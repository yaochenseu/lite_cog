"""Geometric ray returns, not a robot-relative ring of fabricated obstacles.

World XY is the simulation's original map, independent of injected NDT offsets.
No return is emitted for empty range. Occlusion uses the FIRST surface hit.
"""
import math
import numpy as np

AZ,EL=np.meshgrid(np.arange(0,360,2)*math.pi/180,
                 np.array([-30,-20,-15,-12,-9,-6,-3,0,3,6,9,12,20])*math.pi/180)
BASE=np.column_stack((np.cos(EL).ravel()*np.cos(AZ).ravel(),
                      np.cos(EL).ravel()*np.sin(AZ).ravel(),np.sin(EL).ravel()))


def scan(x,y,yaw,boxes=()):
    c,s=math.cos(yaw),math.sin(yaw)
    dirs=BASE.copy()
    dirs[:,0]=c*BASE[:,0]-s*BASE[:,1]
    dirs[:,1]=s*BASE[:,0]+c*BASE[:,1]
    origin=np.array([x+.187*c,y+.187*s,.4])
    distances=np.full(len(dirs),np.inf)
    down=dirs[:,2]<-1e-9
    distances[down]=-.4/dirs[down,2] # actual ground return
    # Room walls plus scene obstacles, all finite-height solids.
    solids=[((-5,-5,0),(-4.9,5,1.5)),((4.9,-5,0),(5,5,1.5)),
            ((-5,-5,0),(5,-4.9,1.5)),((-5,4.9,0),(5,5,1.5))]+list(boxes)
    with np.errstate(divide='ignore',invalid='ignore'):
        for lo,hi in solids:
            near=(np.array(lo)-origin)/dirs
            far=(np.array(hi)-origin)/dirs
            t0=np.max(np.minimum(near,far),axis=1)
            t1=np.min(np.maximum(near,far),axis=1)
            valid=(t1>=np.maximum(t0,0)) & (t0>.15)
            distances[valid]=np.minimum(distances[valid],t0[valid])
    valid=np.isfinite(distances) & (distances>.15) & (distances<=4)
    delta=dirs[valid]*distances[valid,None]
    bx=c*delta[:,0]+s*delta[:,1]
    by=-s*delta[:,0]+c*delta[:,1]
    bz=delta[:,2]
    cp,sp=math.cos(math.pi/10),math.sin(math.pi/10)
    return np.column_stack((cp*bx-sp*bz,by,sp*bx+cp*bz)).astype(np.float32)
