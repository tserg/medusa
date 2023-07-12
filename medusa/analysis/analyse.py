from vyper import ast as vy_ast

from medusa.analysis.base import BaseAnalyser
from medusa.analysis.passes import DeadStoreAnalyser, UnusedImportAnalyser, UnusedParamAnalyser

PASSES = {
    "Dead Store": DeadStoreAnalyser,
    "Unused Import": UnusedImportAnalyser,
    "Unused Function Parameter": UnusedParamAnalyser,
}


def analyse(ast: vy_ast.Module) -> dict[BaseAnalyser, set[vy_ast.VyperNode]]:
    analysis: dict[BaseAnalyser, set[vy_ast.VyperNode]] = {}

    for v in PASSES.values():
        analyser = v()
        analyser.analyse(ast, analysis)

    return analysis
