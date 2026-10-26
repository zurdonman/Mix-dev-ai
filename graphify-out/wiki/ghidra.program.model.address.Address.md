# ghidra.program.model.address.Address

> 59 nodes · cohesion 0.08

## Key Concepts

- **ghidra.program.model.address.Address** (57 connections)
- **ghidra.util.task.TaskMonitor** (19 connections)
- **ghidra.program.model.listing.Program** (15 connections)
- **.matchAArch64RelativeDispatch()** (14 connections) — `rea/bridge/ghidra/ReaGhidraBridge.java`
- **NativeAotExtension** (12 connections) — `rea/bridge/nativeaot/NativeAotExtension.java`
- **.analyze()** (12 connections) — `rea/bridge/nativeaot/NativeAotExtension.java`
- **ghidra.program.model.data.DataType** (10 connections)
- **ReaGhidraExtensions** (10 connections) — `rea/bridge/ghidra/ReaGhidraExtensions.java`
- **NativeAotDirectory.java** (10 connections) — `rea/bridge/nativeaot/NativeAotDirectory.java`
- **.describe()** (10 connections) — `rea/bridge/nativeaot/NativeAotTypeMetadata.java`
- **.recoverAArch64RelativeTable()** (9 connections) — `rea/bridge/ghidra/ReaGhidraBridge.java`
- **NativeAotMethodConventions.java** (8 connections) — `rea/bridge/nativeaot/NativeAotMethodConventions.java`
- **ghidra.program.model.pcode.JumpTable** (7 connections)
- **nativeaot.objectmodel.MethodTableManager** (7 connections)
- **.analyze()** (7 connections) — `rea/bridge/ghidra/ReaGhidraExtensions.java`
- **.inspectDataType()** (7 connections) — `rea/bridge/ghidra/ReaGhidraExtensions.java`
- **.inspectDataType()** (7 connections) — `rea/bridge/nativeaot/NativeAotExtension.java`
- **ReaGhidraApplySeeds** (6 connections) — `rea/bridge/ghidra/ReaGhidraApplySeeds.java`
- **RecoveredAArch64RelativeTable** (6 connections) — `rea/bridge/ghidra/ReaGhidraBridge.java`
- **Located** (6 connections) — `rea/bridge/nativeaot/NativeAotDirectory.java`
- **.locate()** (6 connections) — `rea/bridge/nativeaot/NativeAotDirectory.java`
- **.auditFrozenObjects()** (6 connections) — `rea/bridge/nativeaot/NativeAotExtension.java`
- **.restore()** (6 connections) — `rea/bridge/nativeaot/NativeAotMethodConventions.java`
- **.run()** (5 connections) — `rea/bridge/ghidra/ReaGhidraApplySeeds.java`
- **.dispatchPathDataReferences()** (5 connections) — `rea/bridge/ghidra/ReaGhidraBridge.java`
- *... and 34 more nodes in this community*

## Relationships

- [ReaGhidraBridge](ReaGhidraBridge.md) (53 shared connections)
- [ReaGhidraBridge.java](ReaGhidraBridge.java.md) (36 shared connections)
- [ghidra.program.model.listing.Instruction](ghidra.program.model.listing.Instruction.md) (7 shared connections)
- [ghidra.app.script.GhidraScript](ghidra.app.script.GhidraScript.md) (5 shared connections)
- [ReaSwitchEvidenceProbe](ReaSwitchEvidenceProbe.md) (4 shared connections)
- [ReaGhidraMipsSoftFloat.java](ReaGhidraMipsSoftFloat.java.md) (2 shared connections)
- [ReaFileOffsetSourceProbe](ReaFileOffsetSourceProbe.md) (1 shared connections)
- [MobWar.java](MobWar.java.md) (1 shared connections)

## Source Files

- `rea/bridge/ghidra/ReaGhidraApplySeeds.java`
- `rea/bridge/ghidra/ReaGhidraBridge.java`
- `rea/bridge/ghidra/ReaGhidraExtensions.java`
- `rea/bridge/nativeaot/NativeAotDirectory.java`
- `rea/bridge/nativeaot/NativeAotExtension.java`
- `rea/bridge/nativeaot/NativeAotMethodConventions.java`
- `rea/bridge/nativeaot/NativeAotTypeMetadata.java`

## Audit Trail

- EXTRACTED: 235 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*