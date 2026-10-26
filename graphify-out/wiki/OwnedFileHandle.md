# OwnedFileHandle

> 236 nodes · cohesion 0.02

## Key Concepts

- **OwnedFileHandle** (165 connections) — `rea/src/filesystem/OwnedFileHandle.ts`
- **RegularFile.ts** (118 connections) — `rea/src/filesystem/RegularFile.ts`
- **OwnedRegularFile.ts** (91 connections) — `rea/src/filesystem/OwnedRegularFile.ts`
- **RegularFileCleanupFailure** (82 connections) — `rea/src/filesystem/OwnedRegularFile.ts`
- **JsonFiles.ts** (80 connections) — `rea/src/application/JsonFiles.ts`
- **WebScriptExportService.ts** (77 connections) — `rea/src/application/WebScriptExportService.ts`
- **ManagedStaticProvider.ts** (76 connections) — `rea/src/dotnet/ManagedStaticProvider.ts`
- **LinuxHopperPublisher.ts** (74 connections) — `rea/src/application/LinuxHopperPublisher.ts`
- **RegularFileRead.ts** (67 connections) — `rea/src/application/RegularFileRead.ts`
- **KunaCommand.ts** (62 connections) — `rea/src/kuna/KunaCommand.ts`
- **HopperFileOffset.ts** (61 connections) — `rea/src/hopper/HopperFileOffset.ts`
- **RegularFileChangedError** (56 connections) — `rea/src/filesystem/RegularFile.ts`
- **AnalysisErrorOptions** (54 connections) — `rea/src/domain/analysisErrorBase.ts`
- **regularFileCancellation()** (52 connections) — `rea/src/filesystem/OwnedRegularFile.ts`
- **ManagedSnapshot.ts** (50 connections) — `rea/src/dotnet/ManagedSnapshot.ts`
- **openRegularFile()** (42 connections) — `rea/src/filesystem/RegularFile.ts`
- **NativeCallTarget.ts** (41 connections) — `rea/src/native/NativeCallTarget.ts`
- **AndroidTargetSnapshot.ts** (37 connections) — `rea/src/android/AndroidTargetSnapshot.ts`
- **assertRegularFileActive()** (36 connections) — `rea/src/filesystem/RegularFile.ts`
- **StableFileHash.ts** (35 connections) — `rea/src/filesystem/StableFileHash.ts`
- **PcapSnapshot.ts** (35 connections) — `rea/src/pcap/PcapSnapshot.ts`
- **RegularFileOperationCancelled** (30 connections) — `rea/src/filesystem/RegularFile.ts`
- **hashStableRootArtifact.ts** (26 connections) — `rea/src/artifacts/inventory/hashStableRootArtifact.ts`
- **regularFileCancellation.test.ts** (26 connections) — `rea/tests/boundary/filesystem/regularFileCancellation.test.ts`
- **androidSnapshotClose.test.ts** (26 connections) — `rea/tests/boundary/process/androidSnapshotClose.test.ts`
- *... and 211 more nodes in this community*

## Relationships

- [AnalysisInputError](AnalysisInputError.md) (199 shared connections)
- [analysisErrorCore.ts](analysisErrorCore.ts.md) (161 shared connections)
- [AnalysisError](AnalysisError.md) (117 shared connections)
- [ArtifactReaderFailure](ArtifactReaderFailure.md) (86 shared connections)
- [AnalysisCancelledError](AnalysisCancelledError.md) (55 shared connections)
- [SetupSkill.ts](SetupSkill.ts.md) (53 shared connections)
- [vitest](vitest.md) (52 shared connections)
- [ok](ok.md) (51 shared connections)
- [BinaryTargetResolver.ts](BinaryTargetResolver.ts.md) (41 shared connections)
- [OwnedFileHandle.ts](OwnedFileHandle.ts.md) (36 shared connections)
- [AnalysisProvider.ts](AnalysisProvider.ts.md) (36 shared connections)
- [JadxConfiguration.ts](JadxConfiguration.ts.md) (32 shared connections)

## Source Files

- `rea/src/adb/AdbProvider.ts`
- `rea/src/android/AndroidTargetSnapshot.ts`
- `rea/src/application/BinaryTargetResolver.ts`
- `rea/src/application/ClientConfigurationCleanup.ts`
- `rea/src/application/ClientConfigurationPublication.ts`
- `rea/src/application/JsonFiles.ts`
- `rea/src/application/LinuxHopperPublisher.ts`
- `rea/src/application/RegularFileRead.ts`
- `rea/src/application/SetupHost.ts`
- `rea/src/application/SetupSkill.ts`
- `rea/src/application/SkillFilePublication.ts`
- `rea/src/application/WebScriptExportService.ts`
- `rea/src/application/frida/FridaInstrumentationPort.ts`
- `rea/src/artifacts/ArtifactFileOperation.ts`
- `rea/src/artifacts/ArtifactResourceScope.ts`
- `rea/src/artifacts/RegularFileAdmission.test.ts`
- `rea/src/artifacts/ZipArtifactReader.ts`
- `rea/src/artifacts/inventory/hashStableRootArtifact.ts`
- `rea/src/artifacts/pyinstaller/PyInstallerFileAdmission.test.ts`
- `rea/src/composition/auxiliaryAnalysisProviders.ts`

## Audit Trail

- EXTRACTED: 2133 (98%)
- INFERRED: 40 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*