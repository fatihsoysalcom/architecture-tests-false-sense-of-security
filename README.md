# Architecture Tests False Sense of Security

This Python example demonstrates how static architecture tests can pass (appear 'green') while hiding underlying logical flaws or unintended runtime behaviors. It simulates a scenario where a Service layer incorrectly depends on a Presentation layer, but a simplified architecture test only checks for direct attribute presence, missing the actual violation.

## Language

`python`

## How to Run

Save the code as `architecture_test_demo.py` and run it from your terminal using `python architecture_test_demo.py`.

## Original Article

This example accompanies the Turkish article: [Yeşil Mimari Testler Neden Hataları Kaçırabilir?](https://fatihsoysal.com/blog/yesil-mimari-testler-neden-hatalari-kacirabilir/).

## License

MIT — see [LICENSE](LICENSE).
