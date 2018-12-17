import bpy

ob1 = bpy.data.objects[0]

def uv_Q(ob,mat,num):
    #if(type(ob)!='bpy_types.Object'):
     #   return 0

    if(ob.type != 'MESH'):
        return

    if(num == 99):
        return 0

    for x in ob.data.uv_layers[mat].data:
        x.uv *= 0.5

    if (num == 1):
        for x in ob.data.uv_layers[mat].data:
            x.uv += Vector((0.5,0))
    elif (num == 2):
        for x in ob.data.uv_layers[mat].data:
            x.uv += Vector((0,0.5))
    elif (num == 3):
        for x in ob.data.uv_layers[mat].data:
            x.uv += Vector((0.5,0.5))

def uv_T(ob,mat,num):
    #if(type(ob)!='bpy_types.Object'):
     #   return 0

    if(ob.type != 'MESH'):
        return

    if(num == 99):
        return 0

    for x in ob.data.uv_layers[mat].data:
        a = x.uv[0]
        b = x.uv[1]
        x.uv -= Vector((a*0.666,0))

    if(num == 1):
        for x in ob.data.uv_layers[mat].data:
            x.uv += Vector((0.333,0))
    elif (num == 2):
        for x in ob.data.uv_layers[mat].data:
            x.uv += Vector((0.666,0))

def rename_uvlayer(ob):
    if(ob.type == 'MESH'):
        for uvlayer in ob.data.uv_layers:
            uvlayer.name = ob.material_slots[0].name

def start(ob,mat1,mat2,mat3):

    if(ob.type != 'MESH'):
        return

    if(len(ob.data.uv_layers)<1):
        return

    if(ob.data.uv_layers[0].name == mat1):
        uv_T(ob,mat1,0)

    if(ob.data.uv_layers[0].name == mat2):
        uv_T(ob,mat2,1)

    if(ob.data.uv_layers[0].name == mat3):
        uv_T(ob,mat3,2)

def Run():
    ob = []
    for x in bpy.data.objects:
        ob.append(x)

    for x in ob:
        rename_uvlayer(x)

    for x in ob:
        start(x,'mat10','mat2','mat3')

