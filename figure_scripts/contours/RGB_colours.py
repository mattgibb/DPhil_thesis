# The Transform filter converts any colors to floats, which Paraview cannot handle.
# To convert them back, you can use this:
inp = self.GetInput()
out = self.GetOutput()

numCells  = inp.GetNumberOfCells()
data = inp.GetCellData().GetArray("Colors")

newData = vtk.vtkUnsignedCharArray()
newData.SetName('Colors_converted')
newData.SetNumberOfComponents(3)
for i in range(0, 3*numCells):
    val = int(data.GetValue(i))
    newData.InsertNextValue(val)

out.GetCellData().AddArray(newData)
