# NodeSeaLocation.ts

> 51 nodes · cohesion 0.10

## Key Concepts

- **NodeSeaLocation.ts** (60 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **PeResourceParser.ts** (33 connections) — `rea/src/native/pe/PeResourceParser.ts`
- **parsePeResources()** (20 connections) — `rea/src/native/pe/PeResourceParser.ts`
- **PeResourceLayout.ts** (18 connections) — `rea/src/native/pe/PeResourceLayout.ts`
- **locateNodeSea()** (16 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **readExact()** (13 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **locateThinMachO()** (11 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **scanElfNoteTable()** (11 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **readPeResourceLayout()** (11 connections) — `rea/src/native/pe/PeResourceLayout.ts`
- **formatFailure()** (10 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **locateElfNotes()** (10 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **peFailure()** (9 connections) — `rea/src/native/pe/PeResourceLayout.ts`
- **locatePeResources()** (8 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **readNodeSeaBlob()** (8 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **scanNodeSeaFuse()** (7 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **readPeHeaders()** (7 connections) — `rea/src/native/pe/PeResourceLayout.ts`
- **limitFailure()** (6 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **locateFatMachO()** (6 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **observeNodeSeaFuseMatches()** (5 connections) — `rea/src/artifacts/nodeSea/NodeSeaBlob.ts`
- **hasPeResourceName()** (5 connections) — `rea/src/native/pe/PeResourceLayout.ts`
- **requirePeRange()** (5 connections) — `rea/src/native/pe/PeResourceLayout.ts`
- **collapseRanges()** (4 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **digestRange()** (4 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **readElfTables()** (4 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- **readU32()** (4 connections) — `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- *... and 26 more nodes in this community*

## Relationships

- [ArtifactReaderFailure](ArtifactReaderFailure.md) (26 shared connections)
- [AnalysisInputError](AnalysisInputError.md) (13 shared connections)
- [NodeSeaBlob.ts](NodeSeaBlob.ts.md) (13 shared connections)
- [ok](ok.md) (7 shared connections)
- [go/image.ts](go-image.ts.md) (6 shared connections)
- [PyInstallerArtifactReader.ts](PyInstallerArtifactReader.ts.md) (6 shared connections)
- [ExecutionOptions](ExecutionOptions.md) (6 shared connections)
- [scanCanonical.ts](scanCanonical.ts.md) (5 shared connections)
- [ElfNoteParser.ts](ElfNoteParser.ts.md) (5 shared connections)
- [buffer](buffer.md) (5 shared connections)
- [MachoLoadCommandReader.ts](MachoLoadCommandReader.ts.md) (3 shared connections)
- [PeCertificateParser.test.ts](PeCertificateParser.test.ts.md) (3 shared connections)

## Source Files

- `rea/src/application/binaryDiagnostics/PeResourcesService.test.ts`
- `rea/src/artifacts/nodeSea/NodeSeaBlob.ts`
- `rea/src/artifacts/nodeSea/NodeSeaLocation.ts`
- `rea/src/domain/peOptionalHeader.ts`
- `rea/src/native/pe/PeResourceLayout.ts`
- `rea/src/native/pe/PeResourceParser.test.ts`
- `rea/src/native/pe/PeResourceParser.ts`
- `rea/tests/conformance/providerCompletion.test.ts`

## Audit Trail

- EXTRACTED: 231 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*