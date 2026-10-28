# The open rebuild handbook

**Understand how it works. Build it open. Make it accessible.**

Unfired is for people who want to turn experience into independently built open alternatives. Layoff recovery remains available, but employment status is not a requirement to join.

## Start with a result

| Goal | Read | Produce |
| --- | --- | --- |
| Understand the process | [Method](method.md) | An observation log and behavior contract |
| Choose what to study | [Six tracks](tracks.md) | A scoped first workflow |
| Learn the necessary skills | [12-week curriculum](curriculum.md) | Three completed labs and a project dossier |
| Pick tools | [Tools and primary references](tools.md) | A small, purpose-specific toolkit |
| Validate a replacement | [Compatibility and migration](compatibility.md) | Golden fixtures, a compatibility matrix, and rollback plan |
| Use AI constructively | [AI-assisted rebuilding](ai-workflow.md) | Reviewed code and an evaluation record |
| Keep source reusable | [Licensing](licensing.md) | A license and dependency notice record |
| Ship and maintain | [From prototype to release](release.md) | A reproducible, bounded release |
| Find a useful project | [Project catalog](../projects/README.md) | A proposal with a testable acceptance criterion |
| Improve an existing alternative | [Existing projects](existing-projects.md) | A contribution, adapter, or documented gap |

## A first session

1. Run `python3 -m labs.verify` from a checkout.
2. Choose [one lab](../labs/README.md).
3. Read its contract, then vary one synthetic input and predict the result.
4. Write an observation and an edge case.
5. Propose a small original workflow using `python3 tools/new_project.py my-tool --category workflow --out output/my-tool`.

The scaffold creates ten dossier files. It does not pretend a tool exists or generate passing placeholder tests. Implement the contract and verify it before advertising a product.

For the movement's aims, see [the manifesto](../community/manifesto.md). If you need immediate employment support, start with [the recovery guide](../docs/01-first-72-hours.md).
