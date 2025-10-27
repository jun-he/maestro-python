"""
Python sdk client library.

Example:
    >>> from maestro import Workflow, Job
    >>> wf = Workflow(id="test-wf")
    >>> wf.owner("tester").tags("test")
    >>> wf.job(Job(id="job1", type='NoOp'))
    >>> wf_yaml = wf.to_yaml()
"""

from .dsl.workflow import Workflow
from .dsl.jobs import Job, Subworkflow, Foreach, While

__version__ = "0.1.0"

__all__ = [
    "Job",
    "Subworkflow",
    "Foreach",
    "While",
    "Workflow",
]
