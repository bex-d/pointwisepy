program distswirl
implicit none
character*4 istep
character*50 groupname,filename
integer ::  i,j,ne,np,nbf,ie,in,ip,it,iz,nstart,nstop,nsample,is
integer :: ihex,ipri,ipyr,itet,nfaceq,nfacet,icount,nbp,itest
integer :: ihexf,iprif,ipyrf,itetf,ir,ic,nef,rakel(5,8),swirlel(8)
real :: centre(3),radius,radius1,dist,xcoor,ycoor,zcoor,pi,area,DC60,Machfree,tol
real :: ReStar,swirltan(3,8)
real :: rakecoor(3,5,8),radst(5),swirlcoor(3,8)
integer, allocatable :: ielhex(:,:),ielpri(:,:),ielpyr(:,:)
integer, allocatable :: ieltet(:,:),iface(:,:),iel(:,:),gloloc(:)
integer, allocatable :: ielhexf(:,:),ielprif(:,:),ielpyrf(:,:)
integer, allocatable :: ieltetf(:,:)
real*8, allocatable :: coor(:,:),u(:,:),temp(:,:)
logical :: onemesh,unformatted
data radst(1),radst(2),radst(3),radst(4),radst(5)/ 25,50,70,85,95/

write(6,*) '*******************************************************' 
write(6,*) '*********  DISTORTION & SWIRL ANALYSIS ****************'
write(6,*) '*******************************************************'
write(6,*) 
! write(6,*) 'Enter the filegroup name: '
! read(5,'(a)') groupname
write(6,*) 'OK, reading file group: ', groupname(1:len_trim(groupname))
! READ THE UNFORMATTED .plt FILE
    write(6,*) 'Opening the unformatted .plt file: ', groupname(1:len_trim(groupname))//'.plt'
    open(10,file=groupname(1:len_trim(groupname))//'.plt',form='unformatted',status='old')
    write(*,*) 'opened' 
    read(10) ne,np,nbf
    write(*,*) 'read in ne,np,nbf' 
    write(*,*) 'ne=',ne
    write(*,*) 'np=',np
    write(*,*) 'nbf=',nbf
    allocate (ieltet(4,ne),coor(3,np),iface(5,nbf),u(np,5))
    allocate (ieltetf(4,ne))
    read(10) ((ieltet(in,ie),ie=1,ne),in=1,4) 
    read(10) ((coor(in,ip),ip=1,np),in=1,3)
    read(10) ((iface(in,it),it=1,nbf),in=1,5)
! READ THE UNFORMATTED .unk FILE
  write(6,*) 'Opening the unformatted .unk file: ', groupname(1:len_trim(groupname))//'.unk'
  open(10,file=groupname(1:len_trim(groupname))//'.unk',form='unformatted',status='old')
  write(*,*) 'opened' 
  read(10) np
  read(10) ((u(i,j),i=1,np),j=1,5)
  write(*,*) 'read in unknowns' 
  close(10)
! ASK FOR THE CENTRE COORDINATES AND RADIUS OF THE ANALYSIS PLANE (ASSUMED TO EXIST IN A CONSTANT X PLANE)
  ! write(*,*) 'Enter the x-coordinate of the plane centre: '
  ! read(5,*) centre(1)
  ! write(*,*) 'Enter the y-coordinate of the plane centre: '
  ! read(5,*) centre(2)
  ! write(*,*) 'Enter the z-coordinate of the plane centre: '
  ! read(5,*) centre(3)
  ! write(*,*) 'Enter the tip radius of the analysis plane: '
  ! read(5,*) radius 
  ! write(*,*) 'Enter the freestream Mach number: '
  ! read(5,*) Machfree
  ! write(*,*) 'Enter the freestream Reynolds number: '
  ! read(5,*) ReStar
! FILTER THE ELEMENTS IN THE VICINITY OF THE PLANE 
  nef = 0
  do ie=1,ne
      xcoor = 0.0
      ycoor = 0.0
      zcoor = 0.0
    do in=1,4
      xcoor = xcoor + coor(1,ieltet(in,ie))
      ycoor = ycoor + coor(2,ieltet(in,ie))
      zcoor = zcoor + coor(3,ieltet(in,ie))
    enddo
    xcoor = xcoor/4.
    ycoor = ycoor/4.
    zcoor = zcoor/4.
    dist = sqrt((ycoor-centre(2))**2.+(zcoor-centre(3))**2.)
    if((xcoor.gt.centre(1)-tol).AND.(xcoor.lt.centre(1)+tol).AND.(dist.lt.radius).AND.(dist.gt.radius1))then
      nef = nef + 1
      ieltetf(1:4,nef) = ieltet(1:4,ie)
    endif
  enddo
  write(*,*) 'filtered',nef,'of',ne,'tetrahedra'
  
! CONSTRUCT THE ANALYSIS RAKE
  pi = 3.1416
 
!radst is points at certain % of radius. Modified for ring shaped inlet
  radst(:) = radius1 + (radst(:)/100.)*(radius-radius1)
! loop over the circumferential rake stations
  do ic = 1,8
! loop over the radial stations
    do ir =1,5
      rakecoor(1,ir,ic) = centre(1)	!x coord stays the same			
      rakecoor(2,ir,ic) = centre(2) + radst(ir)*sin((ic-1)*(pi/4.)) !
      rakecoor(3,ir,ic) = centre(3) + radst(ir)*cos((ic-1)*(pi/4.))
    enddo
  enddo
! write the rake coordinates to a file
  filename = 'stencil.txt'
  open(18,file=filename,form='formatted',status='unknown')
  icount=0
  write(18,*) 'Rake Coordinates'
  do ic=1,8
    do ir=1,5
      icount=icount+1
      write(18,102) icount,rakecoor(1,ir,ic),rakecoor(2,ir,ic),rakecoor(3,ir,ic)
    enddo
  enddo
! loop over the 91% radius swirl stations and tangents
  do ic = 1,8
    swirlcoor(1,ic) = centre(1)
    swirlcoor(2,ic) = centre(2) + radius1 + (91./100.)*(radius-radius1)*sin((ic-1)*(pi/4.)) !modified for ring surface
    swirlcoor(3,ic) = centre(3) + radius1 + (91./100.)*(radius-radius1)*cos((ic-1)*(pi/4.)) !modified for ring surface
    swirltan(1,ic) = 0.0
    swirltan(2,ic) = cos((ic-1)*(pi/4.))
    swirltan(3,ic) = -sin((ic-1)*(pi/4.))
  enddo 
  write(18,*) 'Swirl Stations (coords and tangents)'
  icount=0
  do ic=1,8
  icount=icount+1
  write(18,101) ic,swirlcoor(1,ic),swirlcoor(2,ic),swirlcoor(3,ic),swirltan(1,ic),swirltan(2,ic),swirltan(3,ic)
  end do
! FILTER OUT THE RELEVANT ELEMENTS
  call findel(rakecoor,swirlcoor,ieltetf,nef,coor,np,ne,rakel,swirlel    )
! COMPUTE THE DC60 PARAMETER
  call DC60compute(Machfree,ReStar,radst,ne,ieltetf,nef,coor,u,np,rakel,radius )
! COMPUTE THE RADIAL DISTORTION PARAMETER
  call IDR95compute(Machfree,ReStar,radst,ne,ieltetf,nef,coor,u,np,rakel,radius )
! COMPUTE THE SWIRL
  call SWIRLcompute(Machfree,ReStar,radst,ne,ieltetf,nef,coor,u,np,swirlel,swirltan )
! COMPUTE THE EFFICIENCY
  call EFFcompute(Machfree,ReStar,radst,ne,ieltetf,nef,coor,u,np,rakel,radius )
!
  close(18)
101 format(I10,6(f12.5,X))
102 format(I10,3(f12.5,X))

 stop
 end
!----------------------------------------------------------------------------------------------------------
  subroutine DC60compute(Machfree,ReStar,radst,ne,ieltetf,nef&
      &        ,coor,u,np,rakel,radius   )
  implicit none
  integer :: ic,ir,nef,np,rakel(5,8),ie,np1,np2,np3,np4,ne,ieltetf(4,ne),icount
  real :: area,weight,radst(5),coorpt(3),DC60,pi,ptot,gamma,ptotav
  real :: C4,press,speed,Machfree,enstar,ustar,vstar,wstar,speedstar,p0
  real :: denstar,ReStar,mu,Msquared,presstar
  real :: psum(8),psec60(8),p60min,q,qsum,qav,radius
  real*8 :: coor(3,np),u(np,5)
  parameter (gamma=1.4,mu=1.496e-5,pi=3.1416)
! loop over each rake position to compute the area weighted average total pressure
  area = 0.0
  ptot = 0.0
  C4 = 1./4.
  psum = 0.0
  qsum = 0.0
  write(18,*) 'Ptot Values at Rake Points'
  icount=0
  do ic=1,8
    do ir=1,5
      icount=icount+1
      if(ir.eq.1)then
        weight = (45./360.)*pi*((radst(1)+radst(2))/2.)**2.
        area = area + weight
      elseif(ir.eq.5)then
        weight = radst(ir)*(pi/4.)*(radius-0.5*(radst(ir)+radst(ir-1)))
        area = area + weight
      else
        weight = radst(ir)*(pi/4.)*(0.5*(radst(ir+1)+radst(ir))-0.5*(radst(ir)+radst(ir-1)))
        area = area + weight
      endif
      ie=rakel(ir,ic)
      np1 = ieltetf(1,ie)
      np2 = ieltetf(2,ie)
      np3 = ieltetf(3,ie)
      np4 = ieltetf(4,ie)
      if((np1.eq.0).or.(np2.eq.0).or.(np3.eq.0).or.(np4.eq.0)) goto 1000
! compute the mean ptot over the face and the min p60 values
      denstar = C4*(u(np1,1)+u(np2,1)+u(np3,1)+u(np4,1))
      ustar = C4*(u(np1,2)+u(np2,2)+u(np3,2)+u(np4,2))
      vstar = C4*(u(np1,3)+u(np2,3)+u(np3,3)+u(np4,3))
      wstar = C4*(u(np1,4)+u(np2,4)+u(np3,4)+u(np4,4))
      enstar = C4*(u(np1,5)+u(np2,5)+u(np3,5)+u(np4,5))
      speedstar = SQRT(ustar*ustar+vstar*vstar+wstar*wstar)
      press = enstar*denstar*ReStar*ReStar*mu*mu*(gamma-1.)
      presstar = enstar*denstar*(gamma-1.)
      Msquared = (speedstar*speedstar*denstar)/(gamma*presstar)
      p0 = press * (1. + ((gamma-1.)/2.)*Msquared)**(gamma/(gamma-1.))
      write(18,*) icount,p0
      q = p0 - press
      qsum = qsum + q*weight
      ptot = ptot + p0*weight
      psum(ic) = psum(ic) + p0        
 1000 continue
   enddo
 enddo
 psum = psum/5.
 do ic=1,7
   psec60(ic) = 0.5*(psum(ic)+psum(ic+1))
 enddo
 psec60(8) = 0.5*(psum(1)+psum(2))
 write(18,*) 'Sector Average Ptot Values'
 write(18,*) (psec60(ic),ic=1,8)
 ptotav = ptot/area
 qav = qsum/area
 p60min = minval(psec60)
 DC60 = (ptotav - p60min)/qav
 write(6,*)
 write(6,*) '*******************************************************' 
 write(6,*) '            DC60 =', DC60
 write(6,*) '*******************************************************'
 write(6,*)
 end subroutine
!----------------------------------------------------------------------------------------------------------
  subroutine IDR95compute(Machfree,ReStar,radst,ne,ieltetf,nef&
      &        ,coor,u,np,rakel,radius   )
  implicit none
  integer :: ic,ir,nef,np,rakel(5,8),ie,np1,np2,np3,np4,ne,ieltetf(4,ne)
  real :: area,weight,radst(5),coorpt(3),IDR95,pi,ptot,gamma,ptotav
  real :: C4,press,speed,Machfree,enstar,ustar,vstar,wstar,speedstar,p0
  real :: denstar,ReStar,mu,Msquared,presstar
  real :: psum,psec60(8),p95av,q,qsum,qav,radius
  real*8 :: coor(3,np),u(np,5)
  parameter (gamma=1.4,mu=1.496e-5,pi=3.1416)
! loop over each rake position to compute the area weighted average total pressure
  area = 0.0
  ptot = 0.0
  C4 = 1./4.
  psum = 0.0
  do ic=1,8
    do ir=1,5
      if(ir.eq.1)then
        weight = (45./360.)*pi*((radst(1)+radst(2))/2.)**2.
        area = area + weight
      elseif(ir.eq.5)then
        weight = radst(ir)*(pi/4.)*(radius-0.5*(radst(ir)+radst(ir-1)))
        area = area + weight
      else
        weight = radst(ir)*(pi/4.)*(0.5*(radst(ir+1)+radst(ir))-0.5*(radst(ir)+radst(ir-1)))
        area = area + weight
      endif
      ie=rakel(ir,ic)
      np1 = ieltetf(1,ie)
      np2 = ieltetf(2,ie)
      np3 = ieltetf(3,ie)
      np4 = ieltetf(4,ie)
      if((np1.eq.0).or.(np2.eq.0).or.(np3.eq.0).or.(np4.eq.0)) goto 1000
! compute the mean ptot over the face and the min p60 values
      denstar = C4*(u(np1,1)+u(np2,1)+u(np3,1)+u(np4,1))
      ustar = C4*(u(np1,2)+u(np2,2)+u(np3,2)+u(np4,2))
      vstar = C4*(u(np1,3)+u(np2,3)+u(np3,3)+u(np4,3))
      wstar = C4*(u(np1,4)+u(np2,4)+u(np3,4)+u(np4,4))
      enstar = C4*(u(np1,5)+u(np2,5)+u(np3,5)+u(np4,5))
      speedstar = SQRT(ustar*ustar+vstar*vstar+wstar*wstar)
      press = enstar*denstar*ReStar*ReStar*mu*mu*(gamma-1.)
      presstar = enstar*denstar*(gamma-1.)
      Msquared = (speedstar*speedstar*denstar)/(gamma*presstar)
      p0 = press * (1. + ((gamma-1.)/2.)*Msquared)**(gamma/(gamma-1.))
      ptot = ptot + p0*weight
      if(ir.eq.5)then
        psum = psum + p0
      endif        
 1000 continue
   enddo
 enddo
 p95av = psum/8.
 ptotav = ptot/area
 IDR95 = (ptotav - p95av)/ptotav
 write(6,*)
 write(6,*) '*******************************************************' 
 write(6,*) '            IDR95 =', IDR95
 write(6,*) '*******************************************************'
 write(6,*)
 end subroutine
!----------------------------------------------------------------------------------------------------------
  subroutine SWIRLcompute(Machfree,ReStar,radst,ne,ieltetf,nef&
      &        ,coor,u,np,swirlel,swirltan)
  implicit none
  integer :: ic,ir,nef,np,rakel(5,8),ie,np1,np2,np3,np4,ne,ieltetf(4,ne)
  integer :: swirlel(8),icount
  real :: area,weight,radst(5),coorpt(3),IDR95,pi,ptot,gamma,ptotav
  real :: C4,press,speed,Machfree,enstar,ustar,vstar,wstar,speedstar,p0
  real :: denstar,ReStar,mu,Msquared,presstar,angle,SWIRL
  real :: psum,psec60(8),p95av,q,qsum,qav,axial,tangential,swirltan(3,8)
  real*8 :: coor(3,np),u(np,5)
  parameter (gamma=1.4,mu=1.496e-5,pi=3.1416)
! loop over each rake position to compute the area weighted average total pressure
  C4 = 1./4.
  angle = 0.0
  icount=0
  write(18,*) 'Scaled Vels at 91% Ring Points'
  do ic=1,8
      icount=0
      ie=swirlel(ic)
      np1 = ieltetf(1,ie)
      np2 = ieltetf(2,ie)
      np3 = ieltetf(3,ie)
      np4 = ieltetf(4,ie)
      if((np1.eq.0).or.(np2.eq.0).or.(np3.eq.0).or.(np4.eq.0)) goto 1000
      ustar = C4*(u(np1,2)+u(np2,2)+u(np3,2)+u(np4,2))
      vstar = C4*(u(np1,3)+u(np2,3)+u(np3,3)+u(np4,3))
      wstar = C4*(u(np1,4)+u(np2,4)+u(np3,4)+u(np4,4))
      axial = ustar
      tangential = ustar*swirltan(1,ic) + vstar*swirltan(2,ic) + wstar*swirltan(3,ic)
      angle = angle + atan(tangential/axial)
      write(18,100) icount,ustar,vstar,wstar
 1000 continue
 enddo
 angle = angle/8.
 SWIRL = (angle/(2.*pi))*360.
 write(6,*)
 write(6,*) '*******************************************************' 
 write(6,*) '            SWIRL =', SWIRL
 write(6,*) '*******************************************************'
 write(6,*)
!
 100 format(I10,(3f12.5,X))
 end subroutine
!-------------------------------------------------------------------------------------------------------------
  subroutine findel(rakecoor,swirlcoor,ieltetf,nef,coor,np,ne,rakel,swirlel    )
  implicit none
  integer :: i,ic,ir,ie,np,nef,rakel(5,8),ne,ieltetf(4,ne),swirlel(8)
  real :: coorpt(3),C6,vec1(3),vec2(3),vec3(3),vec4(3),ad(3),bc(3),cd(3),tmp(3)
  real :: rakecoor(3,5,8),prod,shape1,shape2,shape3,shape4,voltet
  real :: swirlcoor(3,8)
  real*8 :: coor(3,np)
  C6 = (1./6.)
! loop over the rake stations
  do ic = 1,8
    do ir = 1,5
! loop over the filtered tets
      do ie=1,nef
        vec1(:) = coor(:,ieltetf(1,ie))
        vec2(:) = coor(:,ieltetf(2,ie))
        vec3(:) = coor(:,ieltetf(3,ie))
        vec4(:) = coor(:,ieltetf(4,ie))
        ad(:) = vec1(:) - vec4(:)
        bc(:) = vec2(:) - vec3(:)
        cd(:) = vec3(:) - vec4(:)
        call vcprod(bc,cd,tmp)   !vector product
        call scprod(tmp,ad,prod) !scalar product
        voltet = C6*abs(prod)
! shape1
        vec1(:) = coor(:,ieltetf(1,ie))
        vec2(:) = coor(:,ieltetf(2,ie))
        vec3(:) = coor(:,ieltetf(3,ie))
        vec4(:) = rakecoor(:,ir,ic)
        ad(:) = vec1(:) - vec4(:)
        bc(:) = vec2(:) - vec3(:)
        cd(:) = vec3(:) - vec4(:)
        call vcprod(bc,cd,tmp)   !vector product
        call scprod(tmp,ad,prod) !scalar product
        shape1=C6*abs(prod)/voltet
! shape2
        vec1(:) = coor(:,ieltetf(2,ie))
        vec2(:) = coor(:,ieltetf(3,ie))
        vec3(:) = coor(:,ieltetf(4,ie))
        vec4(:) = rakecoor(:,ir,ic)
        ad(:) = vec1(:) - vec4(:)
        bc(:) = vec2(:) - vec3(:)
        cd(:) = vec3(:) - vec4(:)
        call vcprod(bc,cd,tmp)   !vector product
        call scprod(tmp,ad,prod) !scalar product
        shape2=C6*abs(prod)/voltet
! shape3
        vec1(:) = coor(:,ieltetf(1,ie))
        vec2(:) = coor(:,ieltetf(3,ie))
        vec3(:) = coor(:,ieltetf(4,ie))
        vec4(:) = rakecoor(:,ir,ic)
        ad(:) = vec1(:) - vec4(:)
        bc(:) = vec2(:) - vec3(:)
        cd(:) = vec3(:) - vec4(:)
        call vcprod(bc,cd,tmp)   !vector product
        call scprod(tmp,ad,prod) !scalar product
        shape3=C6*abs(prod)/voltet
! shape4
        vec1(:) = coor(:,ieltetf(1,ie))
        vec2(:) = coor(:,ieltetf(2,ie))
        vec3(:) = coor(:,ieltetf(4,ie))
        vec4(:) = rakecoor(:,ir,ic)
        ad(:) = vec1(:) - vec4(:)
        bc(:) = vec2(:) - vec3(:)
        cd(:) = vec3(:) - vec4(:)
        call vcprod(bc,cd,tmp)   !vector product
        call scprod(tmp,ad,prod) !scalar product
        shape4=C6*abs(prod)/voltet
!
        if((shape1.gt.0.0).and.(shape1.lt.1.0).and.(shape2.gt.0.0).and.(shape2.lt.1.0)&
     &    .and.(shape3.gt.0.0).and.(shape3.lt.1.0).and.(shape4.gt.0.0).and.(shape4.lt.1.0))then
          rakel(ir,ic) = ie
          goto 1000
        endif
      enddo
 1000 continue
    enddo
  enddo
! loop over the swirl stations
 do ic = 1,8
! loop over the filtered tets
   do ie=1,nef
        vec1(:) = coor(:,ieltetf(1,ie))
        vec2(:) = coor(:,ieltetf(2,ie))
        vec3(:) = coor(:,ieltetf(3,ie))
        vec4(:) = coor(:,ieltetf(4,ie))
        ad(:) = vec1(:) - vec4(:)
        bc(:) = vec2(:) - vec3(:)
        cd(:) = vec3(:) - vec4(:)
        call vcprod(bc,cd,tmp)   !vector product
        call scprod(tmp,ad,prod) !scalar product
        voltet = C6*abs(prod)
! shape1
        vec1(:) = coor(:,ieltetf(1,ie))
        vec2(:) = coor(:,ieltetf(2,ie))
        vec3(:) = coor(:,ieltetf(3,ie))
        vec4(:) = swirlcoor(:,ic)
        ad(:) = vec1(:) - vec4(:)
        bc(:) = vec2(:) - vec3(:)
        cd(:) = vec3(:) - vec4(:)
        call vcprod(bc,cd,tmp)   !vector product
        call scprod(tmp,ad,prod) !scalar product
        shape1=C6*abs(prod)/voltet
! shape2
        vec1(:) = coor(:,ieltetf(2,ie))
        vec2(:) = coor(:,ieltetf(3,ie))
        vec3(:) = coor(:,ieltetf(4,ie))
        vec4(:) = swirlcoor(:,ic)
        ad(:) = vec1(:) - vec4(:)
        bc(:) = vec2(:) - vec3(:)
        cd(:) = vec3(:) - vec4(:)
        call vcprod(bc,cd,tmp)   !vector product
        call scprod(tmp,ad,prod) !scalar product
        shape2=C6*abs(prod)/voltet
! shape3
        vec1(:) = coor(:,ieltetf(1,ie))
        vec2(:) = coor(:,ieltetf(3,ie))
        vec3(:) = coor(:,ieltetf(4,ie))
        vec4(:) = swirlcoor(:,ic)
        ad(:) = vec1(:) - vec4(:)
        bc(:) = vec2(:) - vec3(:)
        cd(:) = vec3(:) - vec4(:)
        call vcprod(bc,cd,tmp)   !vector product
        call scprod(tmp,ad,prod) !scalar product
        shape3=C6*abs(prod)/voltet
! shape4
        vec1(:) = coor(:,ieltetf(1,ie))
        vec2(:) = coor(:,ieltetf(2,ie))
        vec3(:) = coor(:,ieltetf(4,ie))
        vec4(:) = swirlcoor(:,ic)
        ad(:) = vec1(:) - vec4(:)
        bc(:) = vec2(:) - vec3(:)
        cd(:) = vec3(:) - vec4(:)
        call vcprod(bc,cd,tmp)   !vector product
        call scprod(tmp,ad,prod) !scalar product
        shape4=C6*abs(prod)/voltet
!
        if((shape1.gt.0.0).and.(shape1.lt.1.0).and.(shape2.gt.0.0).and.(shape2.lt.1.0)&
     &    .and.(shape3.gt.0.0).and.(shape3.lt.1.0).and.(shape4.gt.0.0).and.(shape4.lt.1.0))then
          swirlel(ic) = ie
          goto 2000
        endif
   enddo
 2000 continue
 enddo
!
 end subroutine
!----------------------------------------------------------------------------------------------------------
  subroutine EFFcompute(Machfree,ReStar,radst,ne,ieltetf,nef&
      &        ,coor,u,np,rakel,radius   )
  implicit none
  integer :: ic,ir,nef,np,rakel(5,8),ie,np1,np2,np3,np4,ne,ieltetf(4,ne)
  real :: area,weight,radst(5),coorpt(3),EFF,pi,ptot,gamma,ptotav
  real :: C4,press,speed,Machfree,enstar,ustar,vstar,wstar,speedstar,p0
  real :: denstar,ReStar,mu,Msquared,presstar,radius
  real :: psum(8),psec60(8),p60min,q,qsum,qav,pinfstar,p0star,p0infstar
  real*8 :: coor(3,np),u(np,5)
  parameter (gamma=1.4,mu=1.496e-5,pi=3.1416)
! loop over each rake position to compute the area weighted average total pressure
  area = 0.0
  ptot = 0.0
  C4 = 1./4.
  psum = 0.0
  qsum = 0.0
      pinfstar = 1.0/(gamma*Machfree**2)
      p0infstar = pinfstar*(1.0+0.5*(gamma-1.0)*Machfree*Machfree)**(gamma/(gamma-1.0))
      print*,'pinfstar = ',pinfstar
      print*,'p0infstar = ',p0infstar
  do ic=1,8
    do ir=1,5
      if(ir.eq.1)then
        weight = (45./360.)*pi*((radst(1)+radst(2))/2.)**2.
        area = area + weight
      elseif(ir.eq.5)then
        weight = radst(ir)*(pi/4.)*(radius-0.5*(radst(ir)+radst(ir-1)))
        area = area + weight
      else
        weight = radst(ir)*(pi/4.)*(0.5*(radst(ir+1)+radst(ir))-0.5*(radst(ir)+radst(ir-1)))
        area = area + weight
      endif
      ie=rakel(ir,ic)
      np1 = ieltetf(1,ie)
      np2 = ieltetf(2,ie)
      np3 = ieltetf(3,ie)
      np4 = ieltetf(4,ie)
      if((np1.eq.0).or.(np2.eq.0).or.(np3.eq.0).or.(np4.eq.0)) goto 1000
! compute the mean ptot over the face 
      denstar = C4*(u(np1,1)+u(np2,1)+u(np3,1)+u(np4,1))
      ustar = C4*(u(np1,2)+u(np2,2)+u(np3,2)+u(np4,2))
      vstar = C4*(u(np1,3)+u(np2,3)+u(np3,3)+u(np4,3))
      wstar = C4*(u(np1,4)+u(np2,4)+u(np3,4)+u(np4,4))
      enstar = C4*(u(np1,5)+u(np2,5)+u(np3,5)+u(np4,5))
      speedstar = SQRT(ustar*ustar+vstar*vstar+wstar*wstar)
      press = enstar*denstar*ReStar*ReStar*mu*mu*(gamma-1.)
      presstar = enstar*denstar*(gamma-1.)
      Msquared = (speedstar*speedstar*denstar)/(gamma*presstar)
      p0star = presstar * (1. + ((gamma-1.)/2.)*Msquared)**(gamma/(gamma-1.))
      ptot = ptot + p0star*weight
 1000 continue
   enddo
 enddo
 ptotav = ptot/area
 EFF = ptotav/p0infstar
 write(6,*)
 write(6,*) '*******************************************************' 
 write(6,*) '            Ptot_mean =', ptotav
 write(6,*) '*******************************************************'
 write(6,*)
 write(6,*)
 write(6,*) '*******************************************************' 
 write(6,*) '            EFF =', EFF
 write(6,*) '*******************************************************'
 write(6,*)
 end subroutine
!------------------------------------------------------------------------------------------------------------
 subroutine scprod(v1,v2,prod)
 implicit none
 
 real :: prod,v1(3),v2(3)

 prod = v1(1)*v2(1)+v1(2)*v2(2)+v1(3)*v2(3)

 end subroutine
!-------------------------------------------------------------------------------------------------------------
 subroutine vcprod(v1,v2,v3)
 implicit none
 
 real :: v1(3),v2(3),v3(3)

 v3(1) = v1(2)*v2(3) - v1(3)*v2(2)
 v3(2) = v1(3)*v2(1) - v1(1)*v2(3)
 v3(3) = v1(1)*v2(2) - v1(2)*v2(1)

 end subroutine
!-----------------------------------------------------------------------------------------------------------


