---
linkTitle: "PixelCAD"
type: docs
weight: 1
---
## PixelCAD

Pixel art is awesome. I'm not particularly into retro stuff, but I do love the creativity and challenge that comes from a "less-is-more" kind of medium. Limited space, limited palettes, and implying details where there are none. It's just really cool, and the community is awesome.

There are hundreds of artists out there with some incredible talent for pixel art, both animated and static. In contrast, I am markedly so-so. With enough time and rework, I can draw a solid sprite, but I'm always surprised at how long it takes to tweak, tune, and get things just right. A particular sticking point of mine is sprite-to-sprite consistency. In one composition I may really enjoy outlines, highlights, and edge detection, but in another I find that I've steered away from my own rulebook. It's hard to balance creative expression and "feels good to draw this" when weighed against internal consistency within a larger setting or scene.

Animations, in particular, are a weak spot of mine. For some reason, my brain just cannot compute 3D art rendered from a static angle/frame. It took me maybe 20h of fussing to get a solid walk cycle going with just basic building blocks. Can you imagine a dev building a pixel art game with my kind of skills and impatience? Hah.

In both cases, the reason I find myself stalling or repeating work is consistency. I'm my own worst enemy. 

What I can do, however, is modeling. I enjoy 3D design and am comfortable with CAD. It intuits well to me, but it's not conducive towards pixel art. At least, so I thought.

I'd run across [T3ssl8tr's](https://www.youtube.com/@t3ssel8r) work more than a year ago and was awestruck. What an incredible blend of technical know-how and artistic talent - the dude has some real skills. If you haven't seen his work, take the time to check it out. In short, he built a pipeline that enabled 3D design in Blender and real-time rendering of pixel-perfect art inside Unity. It's slick, because not only can he rapidly prototype, but he can also assign interactions, dynamic lighting, and other major controls inside the engine itself.

Others have created similar pipelines. Probably the best documented is [David Hollands' article](https://www.davidhol.land/articles/3d-pixel-art-rendering/) in Godot. It's not a step-by-step guide, but it lays the groundwork for those who want to attempt the same. Frankly, David and T3ssl8tr have taken the smart approach of rendering inside the game engine. It's the right thing to do if you want dynamic interactions.

Blender-only pipelines exist and are quite impressive in their own right. Typically the primary bifurcation comes from whether compositions are rendered natively at low-resolution or are post-processed in the compositor via resolution downscaling and re-upscaling via nearest neighbor. Toon shading is almost always the de-facto Blender pixel art approach, nearly always done using color-ramps and hand-tweaking.

Some shoutout Blender pixel art examples that I've seen are from [KitagawaGameDev](https://www.youtube.com/watch?v=PBIPJdEECWg) and [Mezaka](https://www.youtube.com/@LarsMezaka). Kitagawa uses a normal's-assisted shadowing technique that is particularly standout, because it yields color banding and tweaking options that are more aligned to hand-drawn pieces than the typical color-ramp approach. Mezaka focuses more on compositor-driven solutions, where images are natively rendered in low-resolution before being post-processed to pick up depth-driven outlines.

## My Blender pipeline

Like any sane person, I made it my mission to create my own CAD -> pixel art system (PixelCAD), with particular focus on outlines. I spent several months in 2025 fixated on this problem and tried to consolidate different Blender-based approaches. Ultimately, I ended up using a native, low-res rendering approach and tons of post-processing. It's a lot of moving parts and not easily captured with words, but below I try to lay out the conceptual overview.

### Camera and Scene settings
Setting up native, low-res pixel art renders is fairly trivial and has been documented several times already. In short:
1. Build your scene, and apply colored materials to objects within the scene. Toon shaders are common and an easy point of entry.
2. Place a camera in the scene that simulates top-down or side-on compositions and use an orthographic lens to avoid depth-based distortion.
3. Tweak the orthographic scale to frame the amount of "zoom" within the composition.
4. Configure the output to natively render at a low-resolution and with some desired aspect ratio (i.e. 256x256).
5. Using EEVEE and only 1x rendered samples, render the piece. Higher sample counts lead to ani-aliasing, which kills pixel-perfect precision and post-processing outline quality.

The key constraint is that every pixel must be deliberate. Anything that introduces blending, resampling, or anti-aliasing breaks downstream post-processing.

### Compositor outline and edge detection post-processing
Outlines and edge detection can be handled many different ways in Blender, it really just depends on how much detail you want from them. In my mind, there are four levels of complexity to post-process pixel-perfect lines:

In my mind, edge detection is best parsed into "external" edge detection and "internal" edge detection. External edges constitute pixels that surround an object or objects to frame them or help distinguish them from background objects. Internal edges are pixels that correspond to concave or convex geometries that are internal to the object bounds.

### External outlines

External edge detection can be further broken down into depth-agnostic outlines and depth-aware outlines.

Depth-agnostic outlines are basically just traces around the object or overlapping objects in the scene. They can be pixel-neutral or pixel-positive. Pixel-neutral outlines means that a natively rendered 16x16 pixel sprite remains 16x16 after post-processing. The outermost collection of pixels are identified and recolored, preserving the native resolution. Pixel-positive outlines add pixels via post-processing, preserving the original sprite and simply adding framing. In a pixel-positive outline, a natively rendered 16x16 sprite will become 18x18 after post-process.

Generally, pixel-neutral outlines involves translating the original sprite through some cardinal kernel (X+1, Y)/(X-1, Y)/(X, Y+1)/(X, Y-1) and subtracting the original image. Re-assembly of the various translations gives the outermost pixels of the original image.

Pixel-positive outlines are even easier and are typically done by dilating the original image with n+1 and simply subtracting the original.

Both pixel-neutral or pixel-positive outlines are great for adding a perimeter around the object or overlapping objects in the scene and give excellent "sticker-like" effects for individual or small groups of sprites. However, neither approach works when trying to distinguish discrete, overlapping objects (such as an object in the foreground and something in the background). Shrubbery looks great because the eye expects foliage to blend and overlap without hard borders. A pile of rocks, however, look blob-like.

Depth-aware outlines is a class of edge detection based on position or depth-passes in Blender. Depth passes are rich with information. Blender can render both a visual pass and a depth pass, which yields positional information about objects in the frame vs the orthographic camera. Objects that are close to the camera have short distances and appear grey or black (i.e. having low value). Distant objects have longer distances and appear more white. In the absence of a background, Blender will render transparent background as infinitely white, seeing how there is "infinite" distance versus the camera.

Similar to the pixel-neutral border approach, the depth pass is translated within some kernel and compared versus the original render. The depth delta-data reveals outlines of overlapping objects in the frame that are separated by some meaningful, user-controlled distance. This is a major advancement over the depth-agnostic approach because multiple objects can be simultaneously rendered in the same scene.

### Internal edge detection

Interior edge detection can be quite complex, albeit the effect does "sell" the pixel art aesthetic. In short, the purpose of interior edge detection is to mathematically apply highlights or accent shadows based on some heuristic settings. It requires combining both a depth pass (discussed above) and a normal-pass. A normal-map is a collection of per-pixel vector data that shows what direction any given pixel is facing. Normals-maps are 3D spatial coordinates and so contain X, Y, and Z elements that define a vector. The X, Y, and Z data is color-mapped to RGB, hence the multi-colored abstraction presentation.

Normal-maps are critical to interior edge detection because they can be used to compare the angles of two adjacent faces that share an edge. If the normals of two adjacent faces are nearly identical (i.e. they face the same direction), then the boundary between them is likely quite soft. In the most extreme example, this might be a curved surface or sphere. In contrast, if the normals of two adjacent faces are orthogonal (i.e. separated by 90 degrees), then it's a pretty crispy corner, as you'd find on a cube.

Ultimately, the problem statement becomes, "what is the minimum required difference in normals to constitute a sharp edge?" There are a few prerequisites to answer this question. The first is to identify all normal-map boundaries. The second is to normalize 3D vector data into a 2D scheme (i.e. hard edge vs soft edge).

At some level of abstraction, identifying the normal-map boundaries is kind of the same problem as finding the external edges of a depth pass. It requires translating the original normal map through some kernel and then looking at the difference between the translated data and the original normal map. Unlike the depth-pass analysis described above, which is just a scalar pixel-to-camera distance, normal-map data is presented in 3D. The cross product of anti-parallel, translated normal maps (i.e. X+1/X-1 and Y+1/Y-1) reveals all possible edges in vector space. "Flattening" the vector data into 2D data is done with simple vector length math. The length of the vector is an analog for the "sharpness" of an edge. Bright lines indicate sharp transitions, while grey or black lines indicate soft edges or no edges at all. It sounds more complicated than it is...

For me, the hardest part was realizing that "negative" magnitudes in Blender are not obvious in the Viewer. Just because a pixel is black doesn't mean it's zero! The clever trick is that the cross-product handles the invisible, negative data. The direction of the resulting vector can be negative, but it's magnitude is positive and made visible. In any case, this approach identifies all internal angles of the rendered object. Then it becomes a trivial user-choice of deciding what is "sharp" vs "non-sharp." This is great if you want to add highlights, as if sun rays were catching a corner; however, there's no parsing of whether the detected edge is concave or convex. A sunbeam glinting off a convex edge makes sense. A glare that comes off a shadowed, concave corner does not.

### Concave vs convex edge parsing

To know which internal edges are concave vs convex, we need to return to the depth pass data. In truth, the original depth delta-data (translation and subtraction process, see above) already has what we need. What took me a while to realize was that convex edges were already being detected using this approach but were just too small to be obvious in the Viewer. Removing the object outline and background before normalizing the remaining depth pass delta data reveals all of the subtler, convex edges. Thresholding these data, the "convex edges depth data" can be used to mask the normals-driven edge detection results. The result is a clean snapshot of convex-edges that can be tuned based on either depth-based thresholding, normals-based "sharpness," or both. Anything that remains in the normals-driven edge detection that are not convex edges are concave surfaces.

## The result?

In truth, I still prefer hand-drawn. And yet, it's a pretty slick approach if you're willing to tune, recolor, and dial-in settings for any given render. The next major milestone would be building a color-based pipeline for a more well-rounded process flow, but that's below my current waterline.

For now, it's a fun little tool that I like to use for splash art and to demo cool "hard surfaces" sort of art. If you found this page via Nucleate, it's what I used to make all the animations inside the app!