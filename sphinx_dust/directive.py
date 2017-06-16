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

        if env.config.dust_include_output:
            written_str = datetime.datetime.strftime(written_on, env.config.dust_datetime_format)
            proofread_str = datetime.datetime.strftime(proofread_on, env.config.dust_datetime_format)

            content = statemachine.StringList([
                _(env.config.dust_output_format).format(written_on=written_str, proofread_on=proofread_str)
            ])
            review_node = review(content, classes=env.config.dust_node_classes)
            review_node += nodes.title(_("Review"), _("Review"))
            self.state.nested_parse(content, self.content_offset, review_node)

            node_list.append(review_node)

        return node_list


def setup(app):
    # Number of days permitted between the doc being written and proofread
    app.add_config_value('dust_days_limit', 30, 'html')
    # Whether to emit warning when a doc needs proofreading
    app.add_config_value('dust_emit_warnings', True, 'html')
    # Whether to include an element in the resulting Sphinx build
    app.add_config_value('dust_include_output', True, 'html')
    # Format string for dust output
    app.add_config_value('dust_output_format', "Written on {written_on}, proofread on {proofread_on}", 'html')
    # The strftime format to use when outputing written-on and proofread-on values
    app.add_config_value('dust_datetime_format', '%d %B %Y', 'html')
    # Classes to apply to the output node
    app.add_config_value('dust_node_classes', ['note'], 'html')

    app.add_node(review, html=(visit_review_node, depart_review_node))
    app.add_directive('reviewer-meta', ReviewerMetaDirective)
