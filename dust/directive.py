import datetime

from docutils import nodes
from docutils import statemachine
from docutils.parsers import rst

from sphinx.util.compat import make_admonition
from sphinx.locale import _


def yearmonthday(value):
    format = "%Y-%m-%d"
    try:
        return datetime.datetime.strptime(value, format)
    except ValueError:
        raise ValueError("Date must respect format {0}".format(format))


class review(nodes.Admonition, nodes.Element):
    """Simple node to generate note elements"""
    pass


def visit_review_node(self, node):
    self.visit_admonition(node)


def depart_review_node(self, node):
    self.depart_admonition(node)


class ReviewerMetaDirective(rst.Directive):
    """Sensor of proofreading needs.

    Each directive is replaced by a note formatting its arguments in a
    human readable sentence. All directives are processed, emitting
    several warnings at once if necessary.
    """
    option_spec = {
        'written-on': yearmonthday,
        'proofread-on': yearmonthday,
    }

    def run(self):
        env = self.state.document.settings.env

        written_on = self.options['written-on']
        proofread_on = self.options['proofread-on']
        delta = proofread_on - written_on

        node_list = []
        if delta.days > env.config.dust_days_limit and env.config.dust_emit_warnings:
            # Don't raise using self.warning because we want to
            # insert the admonition too
            warning = self.state.reporter.warning(
                _("This document hasn't been proofread for {days} days").format(days=delta.days),
            )
            node_list.append(warning)

        written_strf = datetime.datetime.strftime(written_on, _("Written on %d %B %Y"))
        proofread_strf = datetime.datetime.strftime(proofread_on, _("proofread on %d %B %Y"))
        ad = make_admonition(
            review,
            self.name,
            [_("Review")],
            self.options,
            statemachine.StringList([', '.join([written_strf, proofread_strf])]),
            self.lineno,
            self.content_offset,
            self.block_text,
            self.state,
            self.state_machine,
        )
        node_list.append(ad[0])
        return node_list


def setup(app):
    # Number of days permitted between the doc being written and proofread
    app.add_config_value('dust_days_limit', 30, 'html')
    # Whether to emit warning when a doc needs proofreading
    app.add_config_value('dust_emit_warnings', True, 'html')

    app.add_node(review, html=(visit_review_node, depart_review_node))
    app.add_directive('reviewer-meta', ReviewerMetaDirective)
