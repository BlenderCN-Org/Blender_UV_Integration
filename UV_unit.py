import bpy

ob1 = bpy.data.objects[0]

def uv_Q(ob,mat,num):
    #if(type(ob)!='bpy_types.Object'):
     #   return 0

    for ob.data.uv_layers[mat].data:
        x.uv *= 0.5

    if (num == 1):
        for ob.data.uv_layers[mat].data:
            x.uv += Vector((0.5,0))
    elif (num == 2):
        for ob.data.uv_layers[mat].data:
            x.uv += Vector((0,0.5))
    elif (num == 3):
        for ob.data.uv_layers[mat].data:
            x.uv += Vector((0.5,0.5))

def uv_T(ob,mat,num):
    #if(type(ob)!='bpy_types.Object'):
     #   return 0

    for ob.data.uv_layers[mat].data:
        a = x.uv[0]
        b = x.uv[1]
        x.uv -= Vector((a*0.666,0))

    if(num == 1):
        for ob.data.uv_layers[mat].data:
            x.uv += Vector((0.333,0))
    elif (num == 2):
        for ob.data.uv_layers[mat].data:
            x.uv += Vector((0.666,0))

def rename_uvlayer(ob):
    if(ob.type == 'MESH'):
        for uvlayer in ob.data.uv_layers:
            uvlayer.name = ob.material_slots[0].name

