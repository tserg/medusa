from vyper import ast as vy_ast

from medusa.analysis.base import BaseAnalyser


class UnusedParamAnalyser(BaseAnalyser):
    """
    Check for unused function parameters.

    Example:
    ```
    @external
    @pure
    def test(owner: uint256) -> uint256:
        return 1
    ```

    `owner` is never used.
    """

    _id = "Unused Function Parameter"

    def analyse(self, ast: vy_ast.Module, analysis: dict[BaseAnalyser, set[vy_ast.VyperNode]]):

        fn_nodes = ast.get_descendants(vy_ast.FunctionDef)

        for fn_node in fn_nodes:
            fn_params = fn_node.args.args

            for arg_node in fn_params:
                arg_name = arg_node.arg

                # Check for uses but exclude those under a namespace
                arg_name_references = [
                    ref
                    for ref in fn_node.get_descendants(vy_ast.Name, {"id": arg_name})
                    if not isinstance(ref.get_ancestor, vy_ast.Attribute)
                ]
                if not arg_name_references:
                    temp = analysis.get(self, set())
                    temp.add(arg_node)
                    analysis[self] = temp

        return analysis
