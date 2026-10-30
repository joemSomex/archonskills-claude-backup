# Stdio wrapper recursion in long-lived gateways

## Diagnose and reproduce

1. Resolve the running service's actual workspace and interpreter before editing. Back up touched files in the configured scratch directory.
2. When a reply fails in logging setup, inspect the full traceback. Alternating `_SafeWriter.__getattr__` and `_ThreadRoutingStream.__getattr__` frames suggest wrapper accumulation, but do not prove a pointer cycle.
3. Build a deterministic probe with `sys.stdout` and `sys.stderr` temporarily bound to `io.StringIO()`. Repeatedly call `agent.process_bootstrap._install_safe_stdio()` followed by a `agent.thread_scoped_output.thread_scoped_silence()` context for more iterations than the recursion limit, then call `hermes_logging._line_buffer_piped_stdout()`. Restore both original streams in `finally`.
4. Walk known wrapper links iteratively: `_SafeWriter._inner` and `_ThreadRoutingStream._passthrough`. Track object identities and wrapper count. A repeated identity proves a cycle; a growing count without repeats proves acyclic accumulation. Avoid unknown-attribute probes through the suspected chain because delegation itself can recurse.

## Repair and test

1. Make router installation recognize an existing router beneath known transparent safe-writer wrappers rather than installing another router. Adopt its shared routing state while leaving the outer safe writer installed. Do not unwrap arbitrary third-party streams because their behavior may not be transparent.
2. Verify bounded wrapper depth and successful logging setup over the same repeated-installation probe that failed before the patch.
3. Test both installation orders, nested silencing, concurrent unsilenced threads, broken pipes, and temporary global redirects. Preserve shared routing state and exception-swallowing behavior rather than bypassing either wrapper.
4. Run targeted regression and existing logging/output tests. If borrowing tests from another checkout, preserve their platform-selection and isolated-home fixtures; distinguish baseline version mismatches from failures introduced by the patch. Point the test interpreter at the active workspace explicitly rather than installing test dependencies into the live runtime.

## Activate and verify

1. Check for in-flight turns and use the gateway's graceful restart in its existing service scope; do not reset conversations to repair a process-global stream chain.
2. Confirm the expected bot identity reconnects, record the new PID and restart counter, and check that both remain stable.
3. Restrict error inspection to the new startup window so historical recursion traces are not mistaken for a failed repair.
4. Keep a real Discord user-message round trip separate from synthetic regression success and adapter connectivity. If it has not occurred, request a simple test message and label that verification pending.
