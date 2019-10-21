import click
import click_repl
import os
from prompt_toolkit.history import FileHistory
from IndexParser import *
from model import Model

@click.group(invoke_without_command=True)
@click.option('-s', '--sort', default='t', type=str)
@click.option('-f', '--file', default="null", type=str)
@click.option('-db', '--price-db', default="null", type=str)
@click.pass_context
def cli(ctx,sort,file, price_db):
    """Pleasantries CLI"""
    ctx.obj['SORT'] = sort;
    if(price_db != "null"):
        ctx.obj['PRICEDB'] = price_db
    if(file != "null"):
        ctx.obj['FILE'] = file
    if(price_db != "null" and file != "null"):
        #Here generate currency structure TODO
        listFiles = parse_index(ctx.obj['FILE'])
        listTracs = read_files(listFiles)
        ctx.obj['MODEL'] = Model(listTracs,ctx.obj['PRICEDB'])

    #Here generate currency structure TODO
    if ctx.invoked_subcommand is None:
        ctx.invoke(repl)

@cli.command()
@click.pass_context
def balance(ctx):
    """Show account balances."""
    #Here read and print balance TODO...
    click.echo('My ledger balance stuff')

@cli.command()
@click.pass_context
def register(ctx):
    """"Show all transactions with running total."""
    #Here read and print register TODO...
    click.echo('My ledger register stuff')

@cli.command()
@click.pass_context
def printl(ctx):
    """"Print transactions in a format readable by MyLedger."""
    #Here print account in CLI...
    click.echo('My ledger print stuff')

@cli.command()
def repl():
    """Start an interactive session"""
    prompt_kwargs = {
        'history': FileHistory(os.path.expanduser('~/.repl_history'))
    }
    click_repl.repl(click.get_current_context(), prompt_kwargs=prompt_kwargs)

if __name__ == '__main__':
    cli(obj={})