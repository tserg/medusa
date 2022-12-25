from vyper import ast as vy_ast

from medusa.analysis.analyse import analyse
from medusa.vyper.vyper_compile import get_vyper_ast


def extract_errors(analysis: dict[str, set[vy_ast.VyperNode]]) -> dict[str, int]:
    ret = {}

    for analysis_type, errors_flagged in analysis.items():
        error_count = len(errors_flagged)
        ret[analysis_type] = error_count

    return ret


def get_contract_analysis(path: str) -> dict[str, int]:
    vyper_ast = get_vyper_ast(path)
    output_dict = analyse(vyper_ast)
    ret = extract_errors(output_dict)
    return ret
