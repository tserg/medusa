from vyper import ast as vy_ast


def format_analysis(analysis: dict[str, set[vy_ast.VyperNode]]):
    output = ""

    total_count = sum(len(v) for v in analysis.values())

    output += f"""
Total number of errors: {total_count}\n
------------------------------------\n
    """

    for analyser, errors_flagged in analysis.items():
        formatted_errors = "\n\n".join([str(e) for e in errors_flagged])
        output += f"""
Analysis type: {str(analyser)}

{formatted_errors}
------------------------------------\n
        """

    return output


def write_analysis(analysis: str, file_name: str):
    with open(file_name, "w") as fh:
        fh.write(analysis)
