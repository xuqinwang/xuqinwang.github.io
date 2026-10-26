---
title: Publications
permalink: /publications/
---

## Under review

### Adaptively Pivoted Flow Matching for Compositionally Consistent Translation.

**Wang, X.**, Chen, X., Zeller, N., Cremers, D., & Wu, T

*Under review.*

Controlled image translation requires preserving source appearance and maintaining consistency across sequential condition changes. We formulate translation through a shared latent pivot as a translation groupoid and introduce Adaptively Pivoted Flow Matching (AP-FM), which learns adaptive Gaussian priors to reduce conditional velocity ambiguity. The approach improves target fidelity, source appearance preservation, and compositional consistency, evaluated on novel-view synthesis and pose-guided appearance transfer.

### VideoReloc: Long-Term Indoor Video Relocalization against a Kilobyte-Scale Semantic Scene Graph

Li, Q., Chen, X., **Wang, X.**, Zhang, Z., Luo, H., Wu, T., Cremers, D., Liu, L., & Zhang, Y.

*Under review.*

Long-term indoor visual relocalization is challenged by changes in lighting and furniture layouts, which degrade appearance-based localization methods. We propose VideoReloc, a video-based relocalization framework using compact semantic scene graphs (~100 kB per room) instead of appearance-dependent maps. The approach combines adaptive video clips, hypothesis-first registration, and orientation-aware refinement to improve localization robustness and accuracy under scene changes. Evaluated on RIO10 and ReplicaCAD, it achieves higher localization success rates than appearance-based baselines while reducing map storage by approximately two orders of magnitude.

[Paper](https://arxiv.org/abs/2609.21804) · [Project](https://videoreloc.github.io/)

## Published / accepted

### GeodesicNVS: Probability Density Geodesic Flow Matching for Novel View Synthesis.

**Wang, X.**, Wu, T., Zhang, Y., Liu, L., Sun, M., Wang, Y., Zeller, N., & Cremers, D

*CVPR 2026.*

Novel view synthesis methods based on flow matching typically rely on linear latent interpolations that ignore the underlying probability geometry. We introduce probability-density-aware geodesic flow matching to model view transitions along density-consistent trajectories. The approach improves geometric consistency and view synthesis quality while providing a principled connection between probability geometry and generative learning.

[Paper](https://arxiv.org/abs/2603.01010) · [Project](https://xuqinwang.github.io/geodesicNVS.github.io/)

### CinemaTraj: Composing Atomic Camera Trajectories for 3D Scenes with LLM Agents

Li, Q., Chen, X., Türköz, E., Liu, L., **Wang, X.**, Liqiu Meng, Wu, T., Zhang, Y.

*ACM MM 2026.*

Generating cinematic camera trajectories requires both spatial understanding and cinematographic reasoning. CinemaTraj equips an LLM agent with a structured 3D scene graph and decomposes user instructions into atomic camera movements. The framework generates collision-free and prompt-aligned camera trajectories while producing synchronized narrative content.

[Paper](https://arxiv.org/abs/2607.26910) · [Project](https://cinematraj.github.io/)

### MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View Consistent Diffusion

Chen, X., Zhai, Z., Zhou, K., Wang, Z., He, J., Wang, D., Zhang, Y., Sun, M., **Wang, X.**, Westermann, R., Wu, T., Schindler, K., Meng, L.

*DAGM GCPR 2026.*

Textureless city meshes provide geometry but lack realistic appearance, while existing diffusion methods drift across views and misalign with the mesh. MeSS generates a cross-view-consistent 3D Gaussian Splatting scene from mesh-rendered geometric and semantic priors, improving visual consistency and geometry alignment on a city-scale benchmark and transferring zero-shot to a real LoD3 city mesh.

[Paper](https://arxiv.org/abs/2508.15169)  · [Project](https://albertchen98.github.io/mess/)

### GeoSceneGraph: Geometric Scene Graph Diffusion Model for Text-guided 3D Indoor Scene Synthesis

Ruiz, A., Wu, T., Melnik, A., Cheng, Q., **Wang, X.**, Liu, L., Wang, Y., Zhang, Y., & Ritter, H.

*ISPRS 2026 (Oral).*

Text-guided 3D scene generation requires modeling both semantic and geometric relationships between scene objects. GeoSceneGraph combines structured scene graph representations with diffusion-based generation to explicitly encode spatial relationships. This improves controllability and realism for indoor scene synthesis.

[Paper](https://arxiv.org/abs/2511.14884)

### LADB: Latent Aligned Diffusion Bridges for Semi-Supervised Domain Translation.

**Wang, X.**, Wu, T., Zhang, Y., Liu, L., Wang, D., Sun, M., Wang, Y., Zeller, N., & Cremers, D

*DAGM GCPR 2025 (Oral).*

Semi-supervised domain translation often suffers from limited paired data and misaligned latent representations across domains. We propose latent aligned diffusion bridges to learn transport between source and target latent spaces while leveraging abundant unpaired target data. The framework enables more effective cross-domain generation under weak supervision.

[Paper](https://arxiv.org/abs/2509.08628)
