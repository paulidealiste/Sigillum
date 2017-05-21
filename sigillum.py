import click
from mappers.mapreader import letter_reader, ruleset_reader
from mappers.primarybuilder import PrimaryBuilder
from renderers.svgrenderer import SvgRenderer


@click.command()
@click.option(
    '--target', default='./samples/target.txt', type=click.Path(exists=True))
@click.option(
    '--ruleset', default='./samples/ruleset.txt', type=click.Path(exists=True))
@click.option(
    '--svg', default='./default.svg', type=click.Path())
def cli(target, ruleset, svg):
    '''Sligillum transforms writings into visages

    Target file is a common txt file containing text to be transformed.
    Ruleset file contains mapping of letters to numbers which represent
    side numbers of drawn polygons.
    Output consists of an svg file.
    '''
    target_stream = click.open_file(click.format_filename(target), 'r')
    ruleset_stream = click.open_file(click.format_filename(ruleset), 'r')
    pb = PrimaryBuilder()
    with target_stream as f:
        while True:
            chunk = f.readline()
            pb.add_to_letter_list(letter_reader(chunk))
            if not chunk:
                target_stream.close()
                pb.rarefy_letters(200)
                break
    with ruleset_stream as f:
        while True:
            chunk = f.read(1024)
            pb.add_to_rule_dict(ruleset_reader(chunk))
            if not chunk:
                ruleset_stream.close()
                pb.generate_substitute_list()
                pb.generate_substitute_zip()
                render_svg(click.format_filename(svg), pb)
                break


def render_svg(svg_path, linked_object):
    svgr = SvgRenderer(svg_path, linked_object)
    svgr.output_svg()
