# architecture-tests-false-sense-of-security
This Python example demonstrates how static architecture tests can pass (appear 'green') while hiding underlying logical flaws or unintended runtime behaviors. It simulates a scenario where a Service layer incorrectly depends on a Presentation layer, but a simplified architecture test only checks for direct attribute presence, missing the actual vi
