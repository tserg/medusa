from vyper import ast as vy_ast

from medusa.analysis.analyse import analyse
from medusa.vyper.vyper_compile import get_vyper_ast


def extract_errors(analysis: dict[str, set[vy_ast.VyperNode]]) -> dict[str, int]:
    return {str(analyser): len(errors_flagged) for analyser, errors_flagged in analysis.items()}


def get_contract_analysis(path: str) -> dict[str, int]:
    vyper_ast = get_vyper_ast(path)
    output_dict = analyse(vyper_ast)
    return extract_errors(output_dict)
