# maestro-python
Python sdk client library for [Maestro workflow orchestrator](https://github.com/Netflix/maestro).

## Features
 
- Maestro yaml DSL
- Maestro python DSL
- Maestro client
- Maestro command line interface

## Installation

```bash
pip install maestro-sdk
```

Or insall from source:

```bash
git clone https://github.com/jun-he/maestro-python.git
cd maestro-python
pip install -e .
```

## Quick Start

```python
from maestro import Workflow, Job
wf = Workflow(id="test-wf")
wf.owner("tester").tags("test")
wf.job(Job(id="job1", type='NoOp'))
wf_yaml = wf.to_yaml()
```
