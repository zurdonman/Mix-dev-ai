# NativeTraceBudgetTests

> 13 nodes · cohesion 0.15

## Key Concepts

- **NativeTraceBudgetTests** (15 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **.test_launch_flags_preserve_default_debug_and_stop_at_entry()** (4 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **.test_journal_appends_each_row_once_and_flushes_it()** (3 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **Launch()** (2 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **.test_aggregate_trace_budget_admits_exact_boundary_and_rejects_next_record()** (1 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **flush()** (1 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **write()** (1 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **.test_journal_checks_exact_byte_budget_before_writing()** (1 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **GetLaunchFlags()** (1 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **SetLaunchFlags()** (1 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **.test_output_pipe_counts_all_bytes_and_keeps_only_the_prefix()** (1 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **.test_output_pipe_reports_incomplete_capture_after_unexpected_close()** (1 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`
- **.test_oversized_producer_string_is_rejected_before_serialization()** (1 connections) — `rea/bridge/native/test_rea_lldb_tracer.py`

## Relationships

- [.test_invalid_launch_process_reports_explicit_no_creation](test_invalid_launch_process_reports_explicit_no_creation.md) (2 shared connections)
- [subprocess](subprocess.md) (1 shared connections)
- [.test_breakpoint_report_bounds_aggregate_location_json](test_breakpoint_report_bounds_aggregate_location_json.md) (1 shared connections)
- [.test_failed_launch_does_not_infer_exit_from_a_failed_kill](test_failed_launch_does_not_infer_exit_from_a_failed_kill.md) (1 shared connections)
- [.test_failed_launch_publishes_pid_and_retires_live_process](test_failed_launch_publishes_pid_and_retires_live_process.md) (1 shared connections)
- [.test_failed_launch_records_when_valid_process_is_already_exited](test_failed_launch_records_when_valid_process_is_already_exited.md) (1 shared connections)
- [.test_pre_target_integrity_failure_reports_no_process_created](test_pre_target_integrity_failure_reports_no_process_created.md) (1 shared connections)
- [.test_selector_location_report_uses_the_requested_method_type](test_selector_location_report_uses_the_requested_method_type.md) (1 shared connections)

## Source Files

- `rea/bridge/native/test_rea_lldb_tracer.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*