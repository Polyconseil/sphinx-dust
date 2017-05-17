import datetime

from docutils import nodes
from docutils import statemachine
from docutils.parsers import rst
from docutils.parsers.rst.directives.admonitions import BaseAdmonition as make_admonition

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
        delta = datetime.datetime.now() - proofread_on

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

        content = statemachine.StringList([', '.join([written_strf, proofread_strf])])
        review_node = review(content)
        review_node += nodes.title(_("Review"), _("Review"))
        self.state.nested_parse(content, self.content_offset, review_node)

        node_list.append(review_node)
        return node_list


def setup(app):
    # Number of days permitted between the doc being written and proofread
    app.add_config_value('dust_days_limit', 30, 'html')
    # Whether to emit warning when a doc needs proofreading
    app.add_config_value('dust_emit_warnings', True, 'html')

    app.add_node(review, html=(visit_review_node, depart_review_node))
    app.add_directive('reviewer-meta', ReviewerMetaDirective)
