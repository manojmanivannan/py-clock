from .clockFace import TimeGenerator
from .mylogger import logger
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--show','-s',is_flag=True, help="Show the current time")
@click.option('--upper','-u',is_flag=True, help="Show time in upper case")
@click.option('--matrix','-m',is_flag=True, help="Show time as matrix")
def main(show,upper,matrix):
    font_case = 'upper' if upper else 'lower'
    if show:
        
        if matrix:
            logger.info('Getting current time as matrix')
            TimeGenerator('upper' if upper else 'lower').print_time_matrix()
        else:
            logger.info('Getting current time as sentence')
            TimeGenerator('upper' if upper else 'lower').print_time()

if __name__ == '__main__':
    main()