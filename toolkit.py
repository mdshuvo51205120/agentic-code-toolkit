import os
import ast

class CodeAnalyzer:
    """Lightweight AST-based codebase analyzer for open-source repositories."""
    def __init__(self, target_dir="."):
        self.target_dir = target_dir

    def scan_codebase(self):
        issues = []
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    issues.extend(self._analyze_file(full_path))
        return issues

    def _analyze_file(self, filepath):
        file_issues = []
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read(), filename=filepath)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and not ast.get_docstring(node):
                    file_issues.append(f"Missing docstring in function '{node.name}' at {filepath}:{node.lineno}")
        except Exception as e:
            file_issues.append(f"Syntax parsing issue in {filepath}: {str(e)}")
        return file_issues

if __name__ == "__main__":
    print("Agentic Code Toolkit initialized. Ready to inspect repository.")
