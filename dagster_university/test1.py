from pathlib import Path
from dagster_dbt import DbtProject

dbt_project = DbtProject(
  project_dir=Path(__file__).joinpath("..", "..", "analytics").resolve(),
)
print(Path(__file__))
print(Path(__file__).joinpath("..",  "analytics").resolve())