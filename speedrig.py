from __future__ import division
import maya.cmds as my
import pymel.core as pm

def padding( *args ):
    
    list = pm.ls( sl=True )

    num_name_delete = pm.intField(intFieldEntry_num_name_delete, editable = True, query = True, value = True )

    for n in list :

        pm.group( em=True, name= 'empty' )
        pm.parent( 'empty' , n )
        pm.setAttr( 'empty.translateX' , 0)    
        pm.setAttr( 'empty.translateY' , 0)
        pm.setAttr( 'empty.translateZ' , 0)
        pm.setAttr( 'empty.rotateX' , 0)
        pm.setAttr( 'empty.rotateY' , 0)
        pm.setAttr( 'empty.rotateZ' , 0)
        pm.parent( 'empty', world=True )
        pm.parent( n, 'empty' )
                 
        newname= n.split( '_' )
        number_name = len(newname)
                    
        new_name_first= newname[0]+'_'

        for i in range ( 0, number_name ) :

            if i > number_name - num_name_delete-1 or i == number_name - num_name_delete-1 :

                new_name = new_name_first
                print 'naming error'

                break
            
            else :
                            
                if i < number_name - num_name_delete-1 :

                    new_name_second= newname[i+1]+'_'
                    new_name = new_name_first+new_name_second
                    new_name_first= new_name
                                
                else:

                    break
                    
        pm.rename ( 'empty' , new_name + '00_pad' )

    
def rename_lt ( *args ):
    global ori
    ori = 'lt'
    
def rename_ct ( *args ):
    global ori
    ori = 'ct'
    
def rename_rt ( *args ):
    global ori
    ori = 'rt'
    
def renamer ( *args ):
    
    textFieldData_name = pm.textField(textFieldEntry_name, editable = True, query = True, text=True)
    textFieldData_suffix = pm.textField(textFieldEntry_suffix, editable = True, query = True, text=True)
    
    list = pm.ls( sl=True )
    name= textFieldData_name
    count=0
    suffix= textFieldData_suffix
    
    
    for n in list:

        x = len(list)
        
        if x>1 :
            
            count = count+1
            
            if count < x :
                newname = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)
    
            elif count > x-1 :
                newname = '{0}_{1}_{2:02d}_waste'.format(ori, name, count)
    
            else:
                print 'error_on_selected'
        
            pm.rename( n, newname )
                
        else :

            count = count+1
            
            newname = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)
            
                
            pm.rename( n, newname )
            
def renamer_mirror ( *args ):
    
    item_renaming = pm.ls(sl=True, head=1)
    list = pm.ls(sl=True, tail=1)
    
    for n in list:
        newname = n.split( '_' )        
        x = len(newname)
        
        if x == 6 :
            list_mirrored = pm.rename( item_renaming , 'rt' + '_' + newname[1] + '_' + newname[2] + '_' + newname[3] + '_' + newname[4] + '_' + newname[5] )
    
        elif x == 5 :
            list_mirrored = pm.rename( item_renaming , 'rt' + '_' + newname[1] + '_' + newname[2] + '_' + newname[3] + '_' + newname[4] )
            
        elif x == 4 :
            list_mirrored = pm.rename( item_renaming , 'rt' + '_' + newname[1] + '_' + newname[2] + '_' + newname[3] )
    
        else:
            list_mirrored = pm.rename( item_renaming , 'rt' + '_' + newname[1] + '_' + newname[2])
                      
        
def snapping ( *args ):
    
    list= pm.ls(sl=True, head=1)
    groupinto= pm.ls(sl=True, tail=1)
    textFieldData_ik_suffix = pm.textField(textFieldEntry_ik_suffix, editable = True, query = True, text=True)
    ik_suffix = textFieldData_ik_suffix

    num_name_delete = pm.intField(intFieldEntry_num_name_delete, editable = True, query = True, value = True )


    for n in groupinto:

        pm.duplicate(list,name=('snapping'))
        pm.group( 'snapping' , n='readytosnap')
        pm.parent('readytosnap', n)
        pm.setAttr( 'readytosnap.translateX' , 0)    
        pm.setAttr( 'readytosnap.translateY' , 0)
        pm.setAttr( 'readytosnap.translateZ' , 0)
        pm.setAttr( 'readytosnap.rotateX' , 0)
        pm.setAttr( 'readytosnap.rotateY' , 0)
        pm.setAttr( 'readytosnap.rotateZ' , 90)
        pm.parent( 'readytosnap', world=True )
    
        newname= n.split( '_' )
        number_name = len(newname)
                    
        new_name_first= newname[0]+'_'
        
        for i in range ( 0, number_name ) :

            if i > number_name - num_name_delete-1 or i == number_name - num_name_delete-1 :

                new_name = new_name_first
                print 'naming error'
                
                break

            else :
                            
                if i < number_name - num_name_delete-1 :
                    new_name_second= newname[i+1]+'_'
                    new_name = new_name_first+new_name_second
                    new_name_first= new_name
                                
                else:

                    break
                    
        pm.rename ( 'readytosnap' , new_name + '{0}_pad'.format(ik_suffix) )
        pm.rename ( 'snapping' , new_name + '{0}'.format(ik_suffix) )

def dist_dimension_name ( *args ) :

    for i in range (0 , 100) :

        global dist_dimension_created
        
        if pm.objExists ( 'distanceDimension{0}'.format(i+1) ) :

            dist_dimension_created = 'distanceDimension{0}'.format(i+2)

        else :

            dist_dimension_created = 'distanceDimension{0}'.format(i+1)

            break


def IK_Stretch (*args) :

    joint_selected = pm.ls (sl= True)
    joint_start = joint_selected[0]
    joint_end = joint_selected[1]

    textFieldData_ik_suffix = pm.textField(textFieldEntry_ik_suffix, editable = True, query = True, text=True)
    ik_suffix = textFieldData_ik_suffix

    num_name_delete = pm.intField(intFieldEntry_num_name_delete, editable = True, query = True, value = True )


    newname= joint_start.split( '_' )
    print newname
    number_name = len(newname)
                    
    new_name_first= newname[0]+'_'

    for i in range ( 0, number_name ) :

        if i > number_name - num_name_delete-1 or i == number_name - num_name_delete-1 :

            new_name_ik = new_name_first
            print 'naming error'

            break
                
        else :
                            
            if i < number_name - num_name_delete-1 :
                    
                new_name_second= newname[i+1]+'_'
                new_name_ik = new_name_first+new_name_second
                new_name_first= new_name_ik
                                
            else:

                break

    pm.ikHandle ( sj = joint_start ,  ee = joint_end , n= '{0}ik_handle'.format(new_name_ik) )

    if pm.objExists('dist_loc_01') :

        print 'dist_loc_01 exists' 

    else :

        dist_loc_01 = pm.spaceLocator ( n = 'dist_loc_01' )

    for i in range ( 0,20 ) :
        
        if i == 0 :
            
            pm.select (joint_start)
            joint_parent = pm.listRelatives(p=True, type= 'joint')
            
        elif i > 0 :
            
            pm.select (joint_parent)
            joint_first = pm.ls(sl=True)
            joint_parent = pm.listRelatives(p=True, type= 'joint')
            
            if joint_parent == []:

                pm.select(joint_first)
                joint_first_select = pm.ls(sl=True)

                break
                
            else :
                continue

    pm.select ( joint_first_select , hi = True )
    all_hierachy = pm.ls ( sl = True )

    pm.select( joint_start )
    joint_mid = pm.listRelatives(c=True)

    pm.select ( dist_loc_01 , joint_start )
    snapping()
    
    pm.select ( dist_loc_01 , joint_mid )
    snapping()
    
    pm.select ( dist_loc_01 , joint_end )
    snapping()

    pm.select ( joint_start , joint_mid , joint_end)
    ik_joint_loc = pm.ls ( sl = True )
    pm.select ( d = True )

    for n in ik_joint_loc :

        newname= n.split( '_' )
        print newname
        number_name = len(newname)
                        
        new_name_first= newname[0]+'_'

        for i in range ( 0, number_name ) :

            if i > number_name - num_name_delete-1 or i == number_name - num_name_delete-1 :

                new_name = new_name_first
                print 'naming error'

                break
                    
            else :
                                
                if i < number_name - num_name_delete-1 :
                        
                    new_name_second= newname[i+1]+'_'
                    new_name = new_name_first+new_name_second
                    new_name_first= new_name
                                    
                else:

                    break

        print new_name
        pm.select ( '{0}{1}'.format(new_name,ik_suffix) , add = True )

    dist_loc_all = pm.ls ( sl = True)
    dist_loc_start = dist_loc_all[0]
    dist_loc_mid = dist_loc_all[1]
    dist_loc_end = dist_loc_all[2]

    pm.pointConstraint( '{0}'.format(dist_loc_start) , joint_start , mo=True , w = 1 )
    pm.pointConstraint( joint_mid , '{0}_pad'.format(dist_loc_mid) , mo =True , w = 1 )
    pm.pointConstraint( '{0}'.format(dist_loc_end) , '{0}ik_handle'.format(new_name_ik) , mo =True , w = 1 )

    dist_loc_start_tx = pm.getAttr ('{0}_pad.tx'.format(dist_loc_start) )
    dist_loc_start_ty = pm.getAttr ('{0}_pad.ty'.format(dist_loc_start) )
    dist_loc_start_tz = pm.getAttr ('{0}_pad.tz'.format(dist_loc_start) )

    dist_loc_mid_tx = pm.getAttr ('{0}_pad.tx'.format(dist_loc_mid) )
    dist_loc_mid_ty = pm.getAttr ('{0}_pad.ty'.format(dist_loc_mid) )
    dist_loc_mid_tz = pm.getAttr ('{0}_pad.tz'.format(dist_loc_mid) )

    dist_loc_end_tx = pm.getAttr ('{0}_pad.tx'.format(dist_loc_end) )
    dist_loc_end_ty = pm.getAttr ('{0}_pad.ty'.format(dist_loc_end) )
    dist_loc_end_tz = pm.getAttr ('{0}_pad.tz'.format(dist_loc_end) )

    dist_dimension_name()

    pm.distanceDimension( sp = ( dist_loc_start_tx , dist_loc_start_ty , dist_loc_start_tz ) , ep = ( dist_loc_mid_tx , dist_loc_mid_ty , dist_loc_mid_tz ) )

    newname= dist_loc_start.split( '_' )
    print newname
    number_name = len(newname)
                        
    new_name_first= newname[0]+'_'

    for i in range ( 0, number_name ) :

        if i > number_name - num_name_delete-2 or i == number_name - num_name_delete-2 :

            new_name = new_name_first
            print 'naming error'

            break
                    
        else :
                                
            if i < number_name - num_name_delete-2 :
                        
                new_name_second= newname[i+1]+'_'
                new_name = new_name_first+new_name_second
                new_name_first= new_name
                                    
            else:

                break

    dist_measure_01 = pm.rename ( dist_dimension_created , '{0}01_dist'.format(new_name))

    dist_dimension_name()

    pm.distanceDimension( sp = ( dist_loc_mid_tx , dist_loc_mid_ty , dist_loc_mid_tz ) , ep = ( dist_loc_end_tx , dist_loc_end_ty , dist_loc_end_tz ) )

    dist_measure_02 = pm.rename ( dist_dimension_created , '{0}02_dist'.format(new_name))

    dist_dimension_name()

    pm.distanceDimension( sp = ( dist_loc_start_tx , dist_loc_start_ty , dist_loc_start_tz ) , ep = ( dist_loc_end_tx , dist_loc_end_ty , dist_loc_end_tz ) )

    actual_length_ik = pm.rename ( dist_dimension_created , '{0}dist'.format(new_name))

    first_length_ik = pm.getAttr ( '{0}.distance'.format ( dist_measure_01 ) )
    second_length_ik = pm.getAttr ( '{0}.distance'.format ( dist_measure_02 ) )

    max_length_ik = first_length_ik + second_length_ik
            
    ratio_ik_stretch = pm.createNode ( 'multiplyDivide' , n = '{0}ratio_ik_stretch'.format ( new_name ) )
    pm.setAttr ( '{0}.operation'.format ( ratio_ik_stretch ) , 2 )
    pm.connectAttr ( '{0}.distance'.format ( actual_length_ik ) , '{0}.input1X'.format ( ratio_ik_stretch ) )
    pm.setAttr ( '{0}.input2X'.format ( ratio_ik_stretch ) , max_length_ik )

    ratio_ik_stretch_cond = pm.createNode ( 'condition' , n = '{0}ratio_ik_stretch_cond'.format ( new_name ) )
    pm.connectAttr ( '{0}.outputX'.format ( ratio_ik_stretch ) , '{0}.firstTerm'.format ( ratio_ik_stretch_cond ) )
    pm.connectAttr ( '{0}.outputX'.format ( ratio_ik_stretch ) , '{0}.colorIfTrueR'.format ( ratio_ik_stretch_cond ) )
    pm.setAttr ( '{0}.operation'.format ( ratio_ik_stretch_cond ) , 3 )
    pm.setAttr ( '{0}.secondTerm'.format ( ratio_ik_stretch_cond ) , 1 )
    pm.setAttr ( '{0}.colorIfFalseR'.format ( ratio_ik_stretch_cond ) , 1 )

    pm.connectAttr ( '{0}.outColorR'.format ( ratio_ik_stretch_cond ) , '{0}.scaleX'.format( joint_start ) )
    pm.connectAttr ( '{0}.outColorR'.format ( ratio_ik_stretch_cond ) , '{0}.scaleX'.format( joint_mid[0] ) )
    pm.connectAttr ( '{0}.outColorR'.format ( ratio_ik_stretch_cond ) , '{0}.scaleX'.format( joint_end ) )

    pm.delete ( dist_loc_01 )

def squash_stretch_IK ( *args ) :
    
    list_loc = pm.ls(sl=True)
    list_loc_number = len (list_loc)
    

    if pm.objExists('IK_spline_stretch_squash_bind_grp'):
            
        print 'group already exist'
            
    else :

        pm.group(em = True, n='IK_spline_stretch_squash_bind_grp' , w = True)

    if pm.objExists('IK_spline_stretch_squash_IK_handle_grp'):
            
        print 'group already exist'
            
    else :

        pm.group(em = True, n='IK_spline_stretch_squash_IK_handle_grp' , w = True)

    if pm.objExists('IK_spline_stretch_squash_curve_grp') :
            
        print 'group already exist'
            
    else :

        pm.group(em = True, n='IK_spline_stretch_squash_curve_grp' , w = True)

    if pm.objExists('IK_spline_stretch_squash_loc_grp'):
            
        print 'group already exist'
            
    else :

        pm.group(em = True, n='IK_spline_stretch_squash_loc_grp' , w = True)

    if pm.objExists('IK_spline_stretch_squash_joint_ctrl_grp'):
            
        print 'group already exist'
            
    else :

        pm.group(em = True, n='IK_spline_stretch_squash_joint_ctrl_grp' , w = True)


    '''
    Retreiving data entry
    '''

    intFieldData_num_joint = pm.intField( intFieldEntry_num_joint, editable = True, query = True, value = True)
    textFieldData_ik_spline_name = pm.textField(textFieldEntry_ik_spline_name, editable = True, query = True, text=True)
        

    for loc_seq in range ( 1 , list_loc_number + 1 ) :
        

        if loc_seq == list_loc_number :

            print ( list_loc[list_loc_number-1]) , 'is the final locator'

            pm.delete ( list_loc[list_loc_number-1] )

            break

        elif (intFieldData_num_joint % 2) > 0 :

            print 'Input joint number is odd number'

            break

        else :    

            if pm.objExists( '{0}_{1}_IK_spline_loc_grp'.format( textFieldData_ik_spline_name , loc_seq) ) :
                
                print 'Naming error - system with same name exist'

                break
            
            else :

                pm.group ( em = True, n= '{0}_{1}_IK_spline_loc_grp'.format( textFieldData_ik_spline_name , loc_seq) , w = True)
                pm.parent ( '{0}_{1}_IK_spline_loc_grp'.format( textFieldData_ik_spline_name , loc_seq) , 'IK_spline_stretch_squash_loc_grp' )

            loc_first = list_loc[loc_seq-1]
            loc_second = list_loc[loc_seq]
            
            loc_first_X = pm.getAttr(loc_first.translateX)
            loc_first_Y = pm.getAttr(loc_first.translateY)
            loc_first_Z = pm.getAttr(loc_first.translateZ)
            
            loc_second_X = pm.getAttr(loc_second.translateX)
            loc_second_Y = pm.getAttr(loc_second.translateY)
            loc_second_Z = pm.getAttr(loc_second.translateZ)
            
            loc_mid_tranX = loc_first_X + ((loc_second_X - loc_first_X)/2)
            loc_mid_tranY = loc_first_Y + ((loc_second_Y - loc_first_Y)/2)
            loc_mid_tranZ = loc_first_Z + ((loc_second_Z - loc_first_Z)/2)
            
            loc_mid = pm.spaceLocator ( n= '{0}_{1}_02_trans_loc'.format( textFieldData_ik_spline_name , loc_seq))
            pm.setAttr( '{0}.tx'.format(loc_mid) , (loc_mid_tranX))
            pm.setAttr( '{0}.ty'.format(loc_mid) , (loc_mid_tranY))
            pm.setAttr( '{0}.tz'.format(loc_mid) , (loc_mid_tranZ))
            
            if loc_seq == 1 :
        
                pm.rename (loc_first, '{0}_{1}_01_trans_loc'.format( textFieldData_ik_spline_name , loc_seq))
                pm.rename (loc_second, '{0}_{1}_01_trans_loc'.format( textFieldData_ik_spline_name , loc_seq+1))
        
            else :
                pm.rename (loc_second, '{0}_{1}_01_trans_loc'.format( textFieldData_ik_spline_name , loc_seq+1))
        
        
        
            curve_path = pm.curve (d=1 , p = [( loc_first_X , loc_first_Y ,loc_first_Z ),( loc_mid_tranX , loc_mid_tranY , loc_mid_tranZ ),( loc_second_X , loc_second_Y , loc_second_Z )])
        

            '''
            Method on reconstruct curve and rename
            '''   
            pm.rebuildCurve( curve_path , ch=1, rpo=1 , rt=0 , end=1 , kr=0 , kcp=0 , kep=1 , kt=0 , s=intFieldData_num_joint, d=3 , tol=0.0001 )
            name_curve = pm.rename( curve_path , '{0}_{1}_ik_spline_curve'.format( textFieldData_ik_spline_name , loc_seq ) )   
        
        
            pre_joint = ''
            root_joint = ''
        
                    
            for i in range( 0 , intFieldData_num_joint ) :
        
                user_default_unit = pm.currentUnit( query=True, linear=True )
                pm.currentUnit( linear = 'cm' )
                pm.select( cl = True )
                new_joint = pm.joint()
                mot_path = pm.pathAnimation( new_joint , c = curve_path , fm = True )
                pm.cutKey( mot_path + '.u' )
                pm.setAttr( mot_path + '.u', i * ( 1.0 / ( intFieldData_num_joint - 1 )) )
                pm.delete( '{0}.{1}'.format( new_joint , 'tx' ) , icn = True )
                pm.delete( '{0}.{1}'.format( new_joint , 'ty' ) , icn = True )
                pm.delete( '{0}.{1}'.format( new_joint , 'tz' ) , icn = True )
                pm.currentUnit( linear = '{0}'.format(user_default_unit) )
                renaming_item = pm.ls( sl = True )
        
                if i == 0 :
        
                    pre_joint = new_joint
                    root_joint = new_joint
                    pm.rename( renaming_item , '{0}_{1}_{2:02d}_IK_spline_bind'.format( textFieldData_ik_spline_name , loc_seq , i+1 ) )
                    continue
        
                elif i == intFieldData_num_joint -1 :

                    pm.rename( renaming_item , '{0}_{1}_{2:02d}_IK_spline_waste'.format( textFieldData_ik_spline_name , loc_seq , i+1 ) )

                else :
        
                    pm.rename( renaming_item , '{0}_{1}_{2:02d}_IK_spline_bind'.format( textFieldData_ik_spline_name , loc_seq ,i+1 ) )
        
        
        
        
                pm.parent( new_joint , pre_joint )
                pre_joint = new_joint
        
            pm.joint( root_joint, e = True , zso = True, oj = 'xyz' , ch = True , sao = 'yup' )
        
            stretch_squash_ik_handle = pm.ikHandle (sol = 'ikSplineSolver' , pcv = False , ccv = False , c = curve_path , roc = True , ns=2 , sj = ('{0}_{1}_01_IK_spline_bind'.format( textFieldData_ik_spline_name , loc_seq )) , ee = ('{0}_{1}_{2:02d}_IK_spline_bind'.format( textFieldData_ik_spline_name , loc_seq , intFieldData_num_joint-1 )), n = '{0}_{1}_IK_spline'.format( textFieldData_ik_spline_name , loc_seq ))
    
            pre_joint = ''
            root_joint = ''
        
                    
            for i in range( 0 , 3 ) :
        
                user_default_unit = pm.currentUnit( query=True, linear=True )
                pm.currentUnit( linear = 'cm' )
                pm.select( cl = True )
                new_joint = pm.joint()
                mot_path = pm.pathAnimation( new_joint , c = curve_path , fm = True )
                pm.cutKey( mot_path + '.u' )
                pm.setAttr( mot_path + '.u', i * ( 1.0 / 2 ) )
                pm.delete( '{0}.{1}'.format( new_joint , 'tx' ) , icn = True )
                pm.delete( '{0}.{1}'.format( new_joint , 'ty' ) , icn = True )
                pm.delete( '{0}.{1}'.format( new_joint , 'tz' ) , icn = True )
                pm.currentUnit( linear = '{0}'.format(user_default_unit) )
                renaming_item = pm.ls( sl = True )
        
                if i == 0 :
        
                    pre_joint = new_joint
                    root_joint = new_joint
                    pm.rename( renaming_item , '{0}_{1}_{2:02d}_IK_spline_joint_ctrl'.format( textFieldData_ik_spline_name , loc_seq , i+1 ) )
        
                else :
        
                    pm.rename( renaming_item , '{0}_{1}_{2:02d}_IK_spline_joint_ctrl'.format( textFieldData_ik_spline_name , loc_seq ,i+1 ) )
                
                for n in renaming_item :
                    pm.group( em=True, name= 'empty' )
                    pm.parent( 'empty' , n )
                    pm.setAttr( 'empty.translateX' , 0)    
                    pm.setAttr( 'empty.translateY' , 0)
                    pm.setAttr( 'empty.translateZ' , 0)
                    pm.setAttr( 'empty.rotateX' , 0)
                    pm.setAttr( 'empty.rotateY' , 0)
                    pm.setAttr( 'empty.rotateZ' , 0)
                    pm.parent( 'empty', world=True )
                    pm.parent( n, 'empty' )
                    
                for n in renaming_item:
                    
                    newname= n.split( '_' )
                    number_name = len(newname)
                    
                    new_name_first= newname[0]+'_'

                    for i in range ( 0, number_name ) :

                        if i > number_name-3 or i == number_name-3 :

                            new_name = new_name_first
                            print 'naming error'

                            break
                
                        else :
                        
                            if i<number_name-3 :

                                new_name_second= newname[i+1]+'_'
                                new_name = new_name_first+new_name_second
                                new_name_first= new_name
                                
                            else:

                                break
                    
                    pm.rename ( 'empty' , new_name + 'joint_ctrl_pad' )

            stretch_squash_joint_ctrl_grp = pm.group( '{0}_{1}_01_IK_spline_joint_ctrl_pad'.format( textFieldData_ik_spline_name , loc_seq ) , '{0}_{1}_02_IK_spline_joint_ctrl_pad'.format( textFieldData_ik_spline_name , loc_seq ) , '{0}_{1}_03_IK_spline_joint_ctrl_pad'.format( textFieldData_ik_spline_name , loc_seq ) , n = '{0}_{1}_IK_spline_joint_ctrl_grp'.format( textFieldData_ik_spline_name , loc_seq ) )
        

            loc_first_rot = pm.duplicate ( loc_first, n = '{0}_{1}_01_rot_loc'.format( textFieldData_ik_spline_name , loc_seq ))
            loc_mid_rot = pm.duplicate ( loc_mid, n = '{0}_{1}_02_rot_loc'.format( textFieldData_ik_spline_name , loc_seq ))
            loc_second_trans = pm.duplicate ( loc_second, n = '{0}_{1}_03_trans_loc'.format( textFieldData_ik_spline_name , loc_seq ))
            loc_second_rot = pm.duplicate ( loc_second, n = '{0}_{1}_03_rot_loc'.format( textFieldData_ik_spline_name , loc_seq ))
            
            pm.parent (loc_first_rot , loc_first )
            pm.parent (loc_mid_rot , loc_mid )
            pm.parent (loc_second_rot , loc_second_trans[0] )
            
            pm.select ( loc_first , loc_mid , loc_second_trans[0] )
            list_loc_trans = pm.ls(sl= True)
            number_loc_trans = len(list_loc_trans)
            
            for n in list_loc_trans:
                    
                pm.group( em=True, name= 'empty' )
                pm.parent( 'empty' , n )
                pm.setAttr( 'empty.translateX' , 0)    
                pm.setAttr( 'empty.translateY' , 0)
                pm.setAttr( 'empty.translateZ' , 0)
                pm.setAttr( 'empty.rotateX' , 0)
                pm.setAttr( 'empty.rotateY' , 0)
                pm.setAttr( 'empty.rotateZ' , 0)
                pm.parent( 'empty', world=True )
                pm.parent( n, 'empty' )
                    
                newname= n.split( '_' )
                number_name = len(newname)
                    
                new_name_first= newname[0]+'_'

                for i in range ( 0, number_name ) :

                    if i > number_name-1 or i == number_name-1 :

                        new_name = new_name_first
                        print 'naming error'

                        break
                
                    else :

                        if i<number_name-1 :

                            new_name_second= newname[i+1]+'_'
                            new_name = new_name_first+new_name_second
                            new_name_first= new_name
                                
                        else:

                            break
                    
                pm.rename ( 'empty' , new_name + 'pad' )


            pm.parent ( '{0}_{1}_01_trans_loc_pad'.format( textFieldData_ik_spline_name , loc_seq ) , '{0}_{1}_02_trans_loc_pad'.format( textFieldData_ik_spline_name , loc_seq ) , '{0}_{1}_03_trans_loc_pad'.format( textFieldData_ik_spline_name , loc_seq ) ,  '{0}_{1}_IK_spline_loc_grp'.format( textFieldData_ik_spline_name , loc_seq ) )
                
            pm.aimConstraint ( loc_first , loc_mid_rot )
            pm.aimConstraint ( loc_mid , loc_first_rot )
            pm.aimConstraint ( loc_mid , loc_second_rot )
            pm.pointConstraint (loc_first , loc_second_trans[0] , (loc_mid+'_pad') )
                            
            pm.pointConstraint ( loc_first , '{0}_{1}_01_IK_spline_joint_ctrl'.format( textFieldData_ik_spline_name , loc_seq ) , mo=True)
            pm.pointConstraint ( loc_mid , '{0}_{1}_02_IK_spline_joint_ctrl'.format( textFieldData_ik_spline_name , loc_seq ) , mo=True)
            pm.pointConstraint ( loc_second_trans[0] , '{0}_{1}_03_IK_spline_joint_ctrl'.format( textFieldData_ik_spline_name , loc_seq ) , mo=True)
            pm.orientConstraint ( loc_first_rot , '{0}_{1}_01_IK_spline_joint_ctrl'.format( textFieldData_ik_spline_name , loc_seq ) , mo=True)
            pm.orientConstraint ( loc_mid_rot , '{0}_{1}_02_IK_spline_joint_ctrl'.format( textFieldData_ik_spline_name , loc_seq ) , mo=True)
            pm.orientConstraint ( loc_second_rot , '{0}_{1}_03_IK_spline_joint_ctrl'.format( textFieldData_ik_spline_name , loc_seq ) , mo=True)

            curve_length_node = pm.createNode ( 'curveInfo' , n = '{0}curve_length_{1}'.format ( new_name , loc_seq ) )
            pm.connectAttr ( '{0}.worldSpace[0]'.format ( curve_path ) , '{0}.inputCurve'.format( curve_length_node ) )
            curve_arc_length = pm.getAttr ( '{0}.arcLength'.format ( curve_length_node ) )
            
            ratio_curve_stretch = pm.createNode ( 'multiplyDivide' , n = '{0}ratio_curve_stretch_{1}'.format ( new_name , loc_seq ) )
            pm.setAttr ( '{0}.operation'.format ( ratio_curve_stretch ) , 2 )
            pm.connectAttr ( '{0}.arcLength'.format ( curve_length_node ) , '{0}.input1X'.format ( ratio_curve_stretch ) )
            pm.setAttr ( '{0}.input2X'.format ( ratio_curve_stretch ) , curve_arc_length)
            
            ratio_curve_squash = pm.createNode ( 'multiplyDivide' , n = '{0}ratio_curve_squash_{1}'.format ( new_name , loc_seq ) )
            pm.setAttr ( '{0}.operation'.format ( ratio_curve_squash ) , 2 )
            pm.connectAttr ( '{0}.arcLength'.format( curve_length_node ) , '{0}.input2X'.format ( ratio_curve_squash ) )
            pm.setAttr ( '{0}.input1X'.format ( ratio_curve_squash ) , curve_arc_length )
            
            exp_squash = pm.createNode ( 'multiplyDivide' , n = '{0}exp_squash_{1}'.format ( new_name , loc_seq ) )
            pm.setAttr ( '{0}.operation'.format ( exp_squash ) , 2 )
            pm.setAttr ( '{0}.input2X'.format ( exp_squash ) , intFieldData_num_joint-1 ) 
            
            
            for number_joint in range ( 0 , intFieldData_num_joint-1 ) :
                
                pm.connectAttr ( '{0}.outputX'.format ( ratio_curve_stretch ) , '{0}_{1}_{2:02d}_IK_spline_bind.scaleX'.format( textFieldData_ik_spline_name , loc_seq , number_joint+1 ) )
                
                exp_squash_plus = pm.createNode ( 'plusMinusAverage' , n = '{0}exp_squash_plus_0{1}_{2}'.format( new_name , number_joint+1 , loc_seq ) )
                pm.setAttr ( '{0}.input1D[0]'.format( exp_squash_plus ) , 1 )         
                
                if number_joint < (intFieldData_num_joint / 2 ) :
                    
                    pm.setAttr ( '{0}.operation'.format ( exp_squash_plus ) , 1 ) 
                    
                else : 
                
                    pm.setAttr ( '{0}.operation'.format ( exp_squash_plus ) , 2 )
                    
                if number_joint == 0 :
                
                    print 'do nothing'
                    
                elif number_joint > 0 :

                    pm.connectAttr ( '{0}.outputX'.format( exp_squash ) , '{0}.input1D[1]'.format( exp_squash_plus ) )
                    pm.connectAttr ( '{0}exp_squash_plus_0{1}_{2}.output1D'.format( new_name , number_joint , loc_seq ) , '{0}.input1D[0]'.format( exp_squash_plus ) )
                    
                power_curve_squash = pm.createNode ( 'multiplyDivide' , n = '{0}power_curve_squash_0{1}_{2}'.format( new_name , number_joint+1 , loc_seq ) )
                pm.setAttr ( '{0}.operation'.format ( power_curve_squash ) , 3)
                pm.connectAttr ( '{0}.outputX'.format ( ratio_curve_squash ) , '{0}.input1X'.format ( power_curve_squash ) )
                pm.connectAttr ( '{0}.output1D'.format ( exp_squash_plus ) , '{0}.input2X'.format ( power_curve_squash ) )

                pm.connectAttr ( '{0}.outputX'.format ( power_curve_squash ) , '{0}_{1}_{2:02d}_IK_spline_bind.scaleY'.format( textFieldData_ik_spline_name , loc_seq , number_joint+1 ) )
                pm.connectAttr ( '{0}.outputX'.format ( power_curve_squash ) , '{0}_{1}_{2:02d}_IK_spline_bind.scaleZ'.format( textFieldData_ik_spline_name , loc_seq , number_joint+1 ) )
            


            pm.skinCluster('{0}_{1}_01_IK_spline_joint_ctrl'.format( textFieldData_ik_spline_name , loc_seq ),'{0}_{1}_02_IK_spline_joint_ctrl'.format( textFieldData_ik_spline_name , loc_seq ),'{0}_{1}_03_IK_spline_joint_ctrl'.format( textFieldData_ik_spline_name , loc_seq ), '{0}_{1}_ik_spline_curve'.format( textFieldData_ik_spline_name , loc_seq ))

            pm.parent ( curve_path , 'IK_spline_stretch_squash_curve_grp' )
            pm.parent ( '{0}_{1}_01_IK_spline_bind'.format( textFieldData_ik_spline_name , loc_seq ) , 'IK_spline_stretch_squash_bind_grp' )
            pm.parent (  '{0}_{1}_IK_spline'.format( textFieldData_ik_spline_name , loc_seq ) , 'IK_spline_stretch_squash_IK_handle_grp' )
            pm.parent ( stretch_squash_joint_ctrl_grp , 'IK_spline_stretch_squash_joint_ctrl_grp' )


class window_creation_speedrig :
    
    def __init__(self) :
        
        self.create_window()
        
    def create_window(self):
        
        if pm.window('RiggingSpeedUp',exists=True):
            pm.deleteUI('RiggingSpeedUp')

        pm.scriptJob( killAll=True )
        window = pm.window( title="RiggingSpeedUp", iconName="Speed", widthHeight=( 400,400 ) )

        pm.columnLayout( )

        pm.text('Rename', align='center',width=400, height=20, font='boldLabelFont')

        pm.rowColumnLayout( nc=7, cw = [(1,30),(2,30),(3,30),(4,50),(5,100),(6,50),(7,100)] )

        pm.radioCollection()
        pm.radioButton(label = 'lt', editable = True, onCommand = rename_lt)
        pm.radioButton(label = 'rt', editable = True, onCommand = rename_rt)
        pm.radioButton(label = 'ct', editable = True, onCommand = rename_ct)

        global textFieldName_name
        global textFieldEntry_name
        textFieldName_name= pm.text( label= 'Name:')
        textFieldEntry_name = pm.textField(textFieldName_name, editable = True)

        global textFieldName_suffix
        global textFieldEntry_suffix
        textFieldName_suffix= pm.text( label= 'Suffix:')
        textFieldEntry_suffix = pm.textField(textFieldName_suffix, editable = True)

        pm.setParent('..')

        pm.button( label="Apply",width=400, command=renamer )
        pm.button( label="MirrorIntoRt",width=400, command=renamer_mirror )

        pm.separator( h=5, style='none')

        pm.text('Padding&Snapping', align='center',width=400, height=20, font='boldLabelFont')

        global intFieldName_num_name_delete
        global intFieldEntry_num_name_delete

        pm.rowColumnLayout (nc=2, cw = [(1,200) , (2,200)])
        pm.rowColumnLayout (nr= 2 , rh = [(1 , 25) , (2 , 25)] )

        intFieldName_num_name_delete = pm.text( label= 'No_Name_Delete :')
        intFieldEntry_num_name_delete = pm.intField(intFieldName_num_name_delete, editable = True, value=0)

        global textFieldName_ik_suffix
        global textFieldEntry_ik_suffix

        textFieldName_ik_suffix= pm.text( label= 'Suffix:')
        textFieldEntry_ik_suffix = pm.textField(textFieldName_ik_suffix, editable = True)

        pm.setParent( '..' )

        pm.rowColumnLayout (nc=1 , cw = (1,200) )
        pm.button( label="Padding", width=200, command=padding )

        pm.separator( h=5, style='none')

        pm.button( label='Snapping', width = 200, command=snapping )

        pm.separator( h=5, style='none')

        pm.setParent( '..' )
        pm.setParent( '..' )

        pm.text('IK_Stretch', align='center',width=400, height=20, font='boldLabelFont')

        pm.button( label="Stretch IK", width=400, command= IK_Stretch )

        pm.separator( h=5, style='none')

        pm.text('IK_Spline_Stretch&Squash', align='center',width=400, height=20, font='boldLabelFont')

        pm.separator( h=5, style='none')

        pm.rowColumnLayout (nc=4, cw = [ (1,50) , (2,50) , (3,50) , (4,250) ] )

        global intFieldName_num_joint
        global intFieldEntry_num_joint

        intFieldName_num_joint = pm.text( label= 'No_Joint :')
        intFieldEntry_num_joint = pm.intField(intFieldName_num_joint, editable = True, value=0)

        global textFieldName_ik_spline_name
        global textFieldEntry_ik_spline_name

        textFieldName_ik_spline_name= pm.text( label= 'Name:')
        textFieldEntry_ik_spline_name = pm.textField(textFieldName_name, editable = True)

        pm.setParent( '..' )

        pm.button( label="Stretch&Squash IK", width=400, command= squash_stretch_IK )

        window.show()

window_creation_speedrig()