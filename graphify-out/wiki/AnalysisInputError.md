# AnalysisInputError

> 348 nodes · cohesion 0.02

## Key Concepts

- **AnalysisInputError** (507 connections) — `rea/src/domain/analysisErrorCore.ts`
- **AnalysisResourceConstraintError** (331 connections) — `rea/src/domain/analysisErrorCore.ts`
- **analysisErrorWithCleanupFailure()** (249 connections) — `rea/src/domain/analysisErrorCleanup.ts`
- **ArtifactFileOperation.ts** (175 connections) — `rea/src/artifacts/ArtifactFileOperation.ts`
- **GhidraClient.ts** (148 connections) — `rea/src/ghidra/GhidraClient.ts`
- **bindArtifactFileCleanup()** (142 connections) — `rea/src/artifacts/ArtifactFileOperation.ts`
- **AnalysisAccessDeniedError** (123 connections) — `rea/src/domain/analysisErrorCore.ts`
- **AnalysisArtifactChangedError** (123 connections) — `rea/src/domain/analysisErrorCore.ts`
- **stableArtifactConsumers.test.ts** (118 connections) — `rea/tests/process-global/stableArtifactConsumers.test.ts`
- **AnalysisUnsupportedTargetError** (102 connections) — `rea/src/domain/analysisErrorCore.ts`
- **readStableArtifact()** (95 connections) — `rea/src/artifacts/readStableArtifact.ts`
- **artifactFileCancellationCause()** (94 connections) — `rea/src/artifacts/ArtifactFileOperation.ts`
- **investigationProviders.ts** (86 connections) — `rea/src/domain/investigationProviders.ts`
- **Il2cppMetadataProvider.ts** (81 connections) — `rea/src/il2cpp/Il2cppMetadataProvider.ts`
- **AppleDispatchMetadata.ts** (81 connections) — `rea/src/native/AppleDispatchMetadata.ts`
- **.close()** (79 connections) — `rea/src/artifacts/ArtifactResourceScope.ts`
- **fixedAllowanceOptions()** (72 connections) — `rea/src/domain/fixedAllowanceRemediation.ts`
- **ModelArtifactProvider.ts** (70 connections) — `rea/src/model/ModelArtifactProvider.ts`
- **sameRegularFileState()** (69 connections) — `rea/src/filesystem/RegularFile.ts`
- **RustBinaryProvider.ts** (69 connections) — `rea/src/rust/RustBinaryProvider.ts`
- **GoBinaryProvider.ts** (68 connections) — `rea/src/go/GoBinaryProvider.ts`
- **AppleIpsProvider.ts** (68 connections) — `rea/src/native/apple/AppleIpsProvider.ts`
- **readStableArtifact.ts** (67 connections) — `rea/src/artifacts/readStableArtifact.ts`
- **PeImportsProvider.ts** (66 connections) — `rea/src/native/pe/PeImportsProvider.ts`
- **withArtifactRegularFile()** (62 connections) — `rea/src/artifacts/ArtifactFileOperation.ts`
- *... and 323 more nodes in this community*

## Relationships

- [analysisErrorCore.ts](analysisErrorCore.ts.md) (500 shared connections)
- [AnalysisCancelledError](AnalysisCancelledError.md) (253 shared connections)
- [ArtifactReaderFailure](ArtifactReaderFailure.md) (251 shared connections)
- [ExecutionOptions](ExecutionOptions.md) (240 shared connections)
- [OwnedFileHandle](OwnedFileHandle.md) (199 shared connections)
- [ok](ok.md) (109 shared connections)
- [vitest](vitest.md) (107 shared connections)
- [AnalysisError](AnalysisError.md) (99 shared connections)
- [AnalysisOutputError](AnalysisOutputError.md) (69 shared connections)
- [NativeMacOSProvider.ts](NativeMacOSProvider.ts.md) (65 shared connections)
- [AnalysisProvider.ts](AnalysisProvider.ts.md) (61 shared connections)
- [FirmwareProvider.ts](FirmwareProvider.ts.md) (57 shared connections)

## Source Files

- `rea/src/android/JadxProvider.ts`
- `rea/src/apkSignature/apkSignatureFailures.ts`
- `rea/src/apktool/ApktoolWorkspace.lifecycle.test.ts`
- `rea/src/apktool/ApktoolWorkspace.ts`
- `rea/src/application/BinaryTargetResolver.ts`
- `rea/src/application/binaryDiagnostics/AppleIpsService.test.ts`
- `rea/src/application/binaryDiagnostics/ByteEntropyService.ts`
- `rea/src/application/binaryDiagnostics/DevicetreeService.test.ts`
- `rea/src/application/binaryDiagnostics/ElfNotesService.test.ts`
- `rea/src/application/binaryDiagnostics/KernelModuleService.test.ts`
- `rea/src/application/binaryDiagnostics/PeCertificatesService.test.ts`
- `rea/src/application/binaryDiagnostics/PeImportsService.test.ts`
- `rea/src/application/binaryDiagnostics/PeResourcesService.test.ts`
- `rea/src/application/erlang/BeamService.test.ts`
- `rea/src/application/frida/fridaInputErrors.ts`
- `rea/src/artifacts/ArtifactFileOperation.ts`
- `rea/src/artifacts/ArtifactResourceScope.ts`
- `rea/src/artifacts/PyInstallerArtifactReader.ts`
- `rea/src/artifacts/apple/KeyedArchiveReader.ts`
- `rea/src/artifacts/readArtifactFileChunks.ts`

## Audit Trail

- EXTRACTED: 5245 (98%)
- INFERRED: 123 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*