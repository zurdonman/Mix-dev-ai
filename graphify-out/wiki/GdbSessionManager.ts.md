# GdbSessionManager.ts

> 35 nodes · cohesion 0.09

## Key Concepts

- **GdbSessionManager.ts** (79 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **GdbSessionManagerCoverage.test.ts** (44 connections) — `rea/tests/boundary/providers/GdbSessionManagerCoverage.test.ts`
- **parseLinuxProcessStat()** (11 connections) — `rea/src/process/LinuxProcessStat.ts`
- **LinuxProcessStat.ts** (10 connections) — `rea/src/process/LinuxProcessStat.ts`
- **gdbTestHelpers.ts** (7 connections) — `rea/tests/boundary/providers/gdbTestHelpers.ts`
- **gdbOneShotCommandMayInvalidateDetachProof()** (6 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **commandMayChangeInferiorOutput()** (5 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **miStringField()** (5 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **waitForGdbCommandTurn()** (5 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **gdbCommandWord()** (4 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **gdbErrorMessage()** (4 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **GdbExecutableRefusal** (4 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **gdbThreadGroupCount()** (4 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **gdbThreadGroupPids()** (4 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **LinuxProcessStat.test.ts** (4 connections) — `rea/src/process/LinuxProcessStat.test.ts`
- **readLinuxProcessStartTime()** (4 connections) — `rea/src/process/ownedDebuggerSession.ts`
- **gdbCloseUnavailable()** (3 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **gdbConsoleUnavailable()** (3 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **ProcessLifecycle** (3 connections) — `rea/src/process/ProcessLifecycle.ts`
- **createProvider()** (3 connections) — `rea/tests/boundary/providers/GdbSessionManagerCoverage.test.ts`
- **managerFor()** (3 connections) — `rea/tests/boundary/providers/GdbSessionManagerCoverage.test.ts`
- **expectGdbSessionStarted()** (3 connections) — `rea/tests/boundary/providers/gdbTestHelpers.ts`
- **GDB_BUILTIN_ALIASES** (2 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **gdbMiGroupsListSpan()** (2 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **verifyGdbInferiorOutputSink()** (2 connections) — `rea/src/gdb/GdbSessionManager.ts`
- *... and 10 more nodes in this community*

## Relationships

- [GdbSessionManager](GdbSessionManager.md) (31 shared connections)
- [ownedDebuggerSession.ts](ownedDebuggerSession.ts.md) (11 shared connections)
- [vitest](vitest.md) (10 shared connections)
- [ProviderProcess.ts](ProviderProcess.ts.md) (10 shared connections)
- [AnalysisCancelledError](AnalysisCancelledError.md) (7 shared connections)
- [ProcessOwnership.ts](ProcessOwnership.ts.md) (5 shared connections)
- [AnalysisError](AnalysisError.md) (4 shared connections)
- [AnalysisInputError](AnalysisInputError.md) (4 shared connections)
- [RizinDebugSessionManager.ts](RizinDebugSessionManager.ts.md) (4 shared connections)
- [ReverseEngineeringService.ts](ReverseEngineeringService.ts.md) (3 shared connections)
- [analysisErrorCore.ts](analysisErrorCore.ts.md) (3 shared connections)
- [AnalysisTimeoutError](AnalysisTimeoutError.md) (3 shared connections)

## Source Files

- `rea/src/gdb/GdbSessionManager.ts`
- `rea/src/process/LinuxProcessStat.test.ts`
- `rea/src/process/LinuxProcessStat.ts`
- `rea/src/process/ProcessLifecycle.ts`
- `rea/src/process/ownedDebuggerSession.ts`
- `rea/tests/boundary/providers/GdbSessionManagerCoverage.test.ts`
- `rea/tests/boundary/providers/gdbTestHelpers.ts`

## Audit Trail

- EXTRACTED: 178 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*