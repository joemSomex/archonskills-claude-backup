---
name: hermes-stdio-wrapper-debugging
description: "Use when Hermes stdio wrappers recurse. Reproduce topology."
---

# Hermes stdio wrapper recursion

- Resolve the active installed workspace and interpreter from the live gateway before editing; the source checkout may not be the running code.
- Back up touched installed files under the configured scratch directory and leave restart decisions to the controlling operator.
- Reproduce alternating `agent.process_bootstrap._install_safe_stdio()` and `agent.thread_scoped_output.thread_scoped_silence()` over more than the recursion limit, then invoke `hermes_logging._line_buffer_piped_stdout()`.
- Walk `_SafeWriter._inner` and `_ThreadRoutingStream._passthrough` iteratively with an identity set to distinguish an actual cycle from unbounded acyclic wrapper growth. Never probe unknown attributes through a suspected deep chain.
- Keep installation idempotent across known transparent wrappers: a SafeWriter around an existing thread router must not trigger another router installation. Preserve the outer safe wrapper, shared routing state, global redirect behavior, and nested per-thread silencing.
- Test both installation orders, concurrent loud versus silenced threads, broken pipes, and temporary global redirects.
- Installed runtimes may lack pytest and shipped tests. Use an existing managed test interpreter with `PYTHONPATH` explicitly pointing at the active workspace; do not mutate the runtime environment. Copied upstream tests need home isolation and platform marker handling, and newer source-checkout tests can expose unrelated baseline version differences.
