Sphere()
Show()
Render()
 
# Create an animation scene
scene = servermanager.animation.AnimationScene()
# Add one view
scene.ViewModules = [GetActiveView()]

# Create a cue to animate the StartTheta property
cue = servermanager.animation.KeyFrameAnimationCue()
cue.AnimatedProxy = GetActiveSource()
cue.AnimatedPropertyName = "StartTheta"
# Add it to the scene's cues
scene.Cues = [cue]
 
# Create 2 keyframes for the StartTheta track
keyf0 = servermanager.animation.CompositeKeyFrame()
keyf0.Interpolation = 'Ramp'
# At time = 0, value = 0
keyf0.KeyTime = 0
keyf0.KeyValues= [0]
 
keyf1 = servermanager.animation.CompositeKeyFrame()
# At time = 1.0, value = 200
keyf1.KeyTime = 1.0
keyf1.KeyValues= [200]
 
# Add keyframes.
cue.KeyFrames = [keyf0, keyf1]
 
scene.Play()
 
# Some properties you can change
#
# Number of frames used in Sequence mode
# scene.NumberOfFrames = 100
#
# Or you can use real time mode
# scene.PlayMode = 'Real Time'
# scene.Duration = 20
