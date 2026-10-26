# GdbSessionManager

> 43 nodes · cohesion 0.11

## Key Concepts

- **GdbSessionManager** (46 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.#startProtocol()** (28 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.execute()** (21 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.#request()** (19 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.close()** (16 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.start()** (11 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.#retainCleanupFailure()** (10 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.#stopDebuggerOnly()** (10 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **GdbCommandResult** (8 connections) — `rea/src/domain/commandObservation.ts`
- **.#finishSessionCleanup()** (8 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.#receive()** (8 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.#startWithReservation()** (8 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **fixture()** (8 connections) — `rea/tests/boundary/cli/commandEvidenceDelivery.test.ts`
- **snapshotGdbCommandRecords()** (7 connections) — `rea/src/gdb/GdbCommandRecords.ts`
- **.#detachInferior()** (7 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.#failProtocol()** (7 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **fixedDeadlineGuidance()** (5 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.#serialize()** (5 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.#settleExitedCommands()** (5 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.#startReserved()** (5 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **.#stopAfterProtocolFailure()** (5 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **expectDetachProofRevoked()** (5 connections) — `rea/tests/boundary/providers/GdbSessionManagerCoverage.test.ts`
- **startWithVerifiedInferiorTty()** (5 connections) — `rea/tests/boundary/providers/GdbSessionManagerCoverage.test.ts`
- **cancelledWithCallerReason()** (4 connections) — `rea/src/gdb/GdbSessionManager.ts`
- **GdbCommandTimeoutError** (4 connections) — `rea/src/gdb/GdbSessionManager.ts`
- *... and 18 more nodes in this community*

## Relationships

- [GdbSessionManager.ts](GdbSessionManager.ts.md) (31 shared connections)
- [AnalysisError](AnalysisError.md) (18 shared connections)
- [AnalysisCancelledError](AnalysisCancelledError.md) (13 shared connections)
- [ok](ok.md) (11 shared connections)
- [zod](zod.md) (8 shared connections)
- [ownedDebuggerSession.ts](ownedDebuggerSession.ts.md) (6 shared connections)
- [AnalysisTimeoutError](AnalysisTimeoutError.md) (4 shared connections)
- [buffer](buffer.md) (4 shared connections)
- [ReverseEngineeringService.ts](ReverseEngineeringService.ts.md) (3 shared connections)
- [createServer.ts](createServer.ts.md) (3 shared connections)
- [AnalysisInputError](AnalysisInputError.md) (3 shared connections)
- [Evidence](Evidence.md) (2 shared connections)

## Source Files

- `rea/src/domain/commandObservation.ts`
- `rea/src/gdb/GdbCommandRecords.ts`
- `rea/src/gdb/GdbSessionManager.ts`
- `rea/tests/boundary/cli/commandEvidenceDelivery.test.ts`
- `rea/tests/boundary/providers/GdbSessionManagerCoverage.test.ts`
- `rea/tests/boundary/providers/GdbSessionReviewRegressions.test.ts`

## Audit Trail

- EXTRACTED: 212 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*