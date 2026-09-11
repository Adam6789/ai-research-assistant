# AI Research Assistant with Multi-Agent Workflows

A hands-on project demonstrating **agentic AI workflow patterns** using **Google's Agent Development Kit (ADK)**.

## Testing Your Implementation

### Run the Complete Workflow

The workflow can be started directly through Python or, preferably, via the provided `run.sh` script:

```bash
python main.py
```

or

```bash
./run.sh
```

Using `run.sh` provides a convenient entry point for running the application. In addition to starting `main.py`, the script:

* Automatically creates the `logs/` directory if it does not exist.
* Captures both standard output and error output from the application.
* Displays the output in the terminal while simultaneously saving it to a log file.
* Creates a separate, timestamped log file for each execution.
* Uses the Europe/Berlin timezone for consistent log timestamps.

This makes `run.sh` particularly useful for longer-running research workflows, debugging, and comparing results across multiple executions. Running `python main.py` directly is still useful for quick testing when persistent logs are not required.

### Test with Custom Research Queries

Set a custom research query using the environment variable:

```bash
export RESEARCH_QUERY="What are the smartest birds on the planet?"
```

You can then run the workflow using:

```bash
./run.sh
```

Alternatively, run `main.py` directly:

```bash
python main.py
```

Or edit the `queries` list in `main.py` to add your own research topics.

### Expected Output

If your implementation is correct, you should see:

1. All 7 stages execute successfully
2. `LoopAgent`, `ParallelAgent`, and `SequentialAgent` objects created
3. LLM output from Gemini
4. Performance evaluation metrics displayed
5. A generated `research_report.md` file with comprehensive findings

When using `./run.sh`, the same output is also persisted in the `logs/` directory with a timestamp corresponding to the execution time.

### Actual Output

I ran the code with the following query:

> "The impact of emperor Constantine the Great on the quality of Europe."

The run met all expectations. However, I was not able to decrease the time as I had to increase the maximal amount of output tokens to avoid getting responses that are truncated and can therefore not be turned into json objects.
