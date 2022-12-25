from vyper import ast as vy_ast


def format_analysis(analysis: dict[str, set[vy_ast.VyperNode]]):
    output = ""

    total_count = sum(len(v) for v in analysis.values())

    output += f"""
Total number of errors: {total_count}\n
------------------------------------\n
    """

    for analysis_type, errors_flagged in analysis.items():
        formatted_errors = "\n\n".join([str(e) for e in errors_flagged])
        output += f"""
Analysis type: {analysis_type}

{formatted_errors}
------------------------------------\n
        """

    return output


def write_analysis(analysis: str, file_name: str):
    f = open(file_name, "w")
    f.write(analysis)
