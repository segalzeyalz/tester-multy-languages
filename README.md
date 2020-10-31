# **Tests for multiple languages**

## Motivation
There are huge amount of testing ways as each language adopt it's own solution for it. 
As I see it now the best way to test should looks like jest:
expect(exp).toBe(assertion).
This repo only focus on that: testing in readable way for multiple languages;

## Basic Usage
simply import the package, and use the expect function. Nothing than that.
For python it looks like that:
```python
from python_project.python_tester import expect
expect(5).to_be(5)
```
