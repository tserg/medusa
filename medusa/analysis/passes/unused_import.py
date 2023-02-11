from vyper import ast as vy_ast

from medusa.analysis.base import BaseAnalyser


class UnusedImportAnalyser(BaseAnalyser):
    """
    Check for unused imports.

    Example:
    ```
    from vyper.interfaces import ERC20
    ```

    `ERC20` is never used.

    This pass does not work for custom interfaces yet.
    """

    _id = "Unused Import"

    def analyse(self, ast: vy_ast.Module, analysis: dict[BaseAnalyser, set[vy_ast.VyperNode]]):

        import_nodes = ast.get_descendants((vy_ast.Import, vy_ast.ImportFrom))

        for n in import_nodes:
            if isinstance(n, vy_ast.Import):
                interface_name = n.alias
            elif isinstance(n, vy_ast.ImportFrom):
                interface_name = n.name

            # Check for `implements`
            is_implemented = (
                len(
                    ast.get_descendants(
                        vy_ast.AnnAssign,
                        {"target.id": "implements", "annotation.id": interface_name},
                    )
                )
                > 0
            )

            # Check for usage as `Interface(address).function()`
            is_used = len(ast.get_descendants(vy_ast.Call, {"func.id": interface_name})) > 0

            if not is_implemented and not is_used:
                temp = analysis.get(self, set())
                temp.add(n)
                analysis[self] = temp

        return analysis
