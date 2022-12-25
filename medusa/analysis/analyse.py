from vyper import ast as vy_ast

from medusa.analysis.base import BaseAnalyser
from medusa.analysis.passes import DeadStoreAnalyser

PASSES = {"Dead Store": DeadStoreAnalyser}


def analyse(ast: vy_ast.Module) -> dict[BaseAnalyser, set[vy_ast.VyperNode]]:
    analysis: dict[BaseAnalyser, set[vy_ast.VyperNode]] = {}

    for k, v in PASSES.items():
        analyser = v()
        analyser.analyse(ast, analysis)

    print("analysis: ", analysis)

    return analysis
