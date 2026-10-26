# JavaScriptSemanticGraphBuilder.ts

> 156 nodes · cohesion 0.04

## Key Concepts

- **JavaScriptSemanticGraphBuilder.ts** (116 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphBuilder.ts`
- **JavaScriptSemanticGraphConstruction.ts** (58 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphConstruction.ts`
- **JavaScriptSemanticGraphFlowProjection.ts** (46 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphFlowProjection.ts`
- **JavaScriptSemanticGraphBuilder.test.ts** (39 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphBuilder.test.ts`
- **addSemanticGraphRelation()** (35 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphConstruction.ts`
- **createJavaScriptSemanticGraphProjection()** (31 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphBuilder.ts`
- **retainSemanticGraphNode()** (31 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphConstruction.ts`
- **JavaScriptSemanticGraphDataProjection.ts** (30 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphDataProjection.ts`
- **JavaScriptSemanticGraphNode** (29 connections) — `rea/src/domain/javascript/javascriptSemanticGraphSchemas.ts`
- **JavaScriptSemanticGraphObjectProjection.ts** (28 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphObjectProjection.ts`
- **JavaScriptSemanticGraphAsyncProjection.ts** (26 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphAsyncProjection.ts`
- **addSemanticGraphUnknown()** (26 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphConstruction.ts`
- **JavaScriptSemanticGraphValueProjection.ts** (26 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphValueProjection.ts`
- **JavaScriptSemanticUnknownCapacity.test.ts** (26 connections) — `rea/src/application/javascript/JavaScriptSemanticUnknownCapacity.test.ts`
- **JavaScriptSemanticGraphChildProcessProjection.ts** (24 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphChildProcessProjection.ts`
- **JavaScriptSemanticGraphEvidence.ts** (24 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphEvidence.ts`
- **unknownSemanticEvidence()** (24 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphEvidence.ts`
- **JavaScriptSemanticGraphProjection.ts** (24 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphProjection.ts`
- **javascriptSourceCoordinates.ts** (24 connections) — `rea/src/domain/javascript/javascriptSourceCoordinates.ts`
- **SemanticFlowProjectionContext** (18 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphFlowProjection.ts`
- **JavaScriptSemanticGraphResourceProjection.ts** (16 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphResourceProjection.ts`
- **projectFileSteps()** (14 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphBuilder.ts`
- **JavaScriptSemanticGraphElectronProjection.ts** (14 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphElectronProjection.ts`
- **JavaScriptSemanticGraphFingerprintProjection.ts** (14 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphFingerprintProjection.ts`
- **JavaScriptSemanticGraphAssignmentProjection.ts** (13 connections) — `rea/src/application/javascript/JavaScriptSemanticGraphAssignmentProjection.ts`
- *... and 131 more nodes in this community*

## Relationships

- [javascript/javascriptSemanticGraph.ts](javascript-javascriptSemanticGraph.ts.md) (91 shared connections)
- [compositeKey](compositeKey.md) (42 shared connections)
- [resolveSemanticBindingState](resolveSemanticBindingState.md) (38 shared connections)
- [compareUnicodeCodePoints](compareUnicodeCodePoints.md) (33 shared connections)
- [javascriptSemanticAnalysis.ts](javascriptSemanticAnalysis.ts.md) (18 shared connections)
- [javascriptStaticAnalysisHelpers.ts](javascriptStaticAnalysisHelpers.ts.md) (14 shared connections)
- [JavaScriptArtifactAnalysis.ts](JavaScriptArtifactAnalysis.ts.md) (11 shared connections)
- [ref_node_crypto](ref_node_crypto.md) (11 shared connections)
- [javascriptStaticAnalysis.ts](javascriptStaticAnalysis.ts.md) (9 shared connections)
- [javascriptSemanticRequireOrigin.ts](javascriptSemanticRequireOrigin.ts.md) (7 shared connections)
- [JavaScriptAnalysisWorkerSchemas.ts](JavaScriptAnalysisWorkerSchemas.ts.md) (6 shared connections)
- [JavaScriptAnalysisWorker.ts](JavaScriptAnalysisWorker.ts.md) (5 shared connections)

## Source Files

- `rea/src/application/javascript/JavaScriptSemanticGraphAssignmentProjection.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphAsyncProjection.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphBuilder.test.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphBuilder.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphChildProcessProjection.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphConstruction.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphDataProjection.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphElectronProjection.test.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphElectronProjection.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphEvidence.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphFingerprintProjection.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphFlowProjection.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphObjectProjection.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphProjection.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphResourceProjection.ts`
- `rea/src/application/javascript/JavaScriptSemanticGraphValueProjection.ts`
- `rea/src/application/javascript/JavaScriptSemanticUnknownCapacity.test.ts`
- `rea/src/domain/javascript/javascriptSemanticGraph.ts`
- `rea/src/domain/javascript/javascriptSemanticGraphSchemas.ts`
- `rea/src/domain/javascript/javascriptSemanticReturns.ts`

## Audit Trail

- EXTRACTED: 820 (98%)
- INFERRED: 16 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*