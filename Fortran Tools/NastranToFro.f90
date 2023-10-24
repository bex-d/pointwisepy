program NastranToFro

     implicit none 
     character*4 istep,fileExtension,dummy 
     character*50 nasfile,frofile
     character*80 string,string1, string2, string3
     integer ::  i,j,ne,np,nbf,ie,in,ip,it,iz,nstart,nstop,nsample,is,np2,isur, Element2
     integer :: ihex,ipri,ipyr,itet,nfaceq,nfacet,icount,itest,tmp,int,nsegm 
     integer :: ip1, ip2, ip3,nPshell
     integer :: nsurf,test,surfno,nbp,isurf,itri,i1,i2,i3,i4,i5,i6,ipx,nsur
     integer, allocatable :: ielhex(:,:),ielpri(:,:),ielpyr(:,:),trino(:),surf_con(:,:) 
     integer, allocatable :: ieltet(:,:),iface(:,:),iel(:,:),gloloc(:),iface_new(:,:) 
     real*4 :: Mach,ss,T,gamma,uinf,press,R,cp,dens
     real*4 :: x,y,z
     real*4, allocatable :: u(:,:),uabs(:,:),coor(:,:),temporary(:,:),uloc(:,:),coor_new(:,:)
     logical :: onemesh,unformatted 
	 integer :: el2
	 integer :: i7, ierr, num_lines
	 character*256, allocatable :: array1(:)
	 
     write(6,*) '*******************************************************' 
     write(6,*) '*****  SURFACE MESH .nas -> .fro CONVERTER  ***********'
     write(6,*) '*******************************************************'
     write(6,*) 
     write(6,*) 'Enter the .nas filename (not including .nas): '
     read(5,'(a)') nasfile

     write(6,*) 'Opening the .nas file: ', nasfile
     open(10,file=nasfile(1:len_trim(nasfile))//'.nas',form='formatted',status='old')
     write(*,*) 'opened' 
     read(10,*) string
     read(10,*)
     close(10)

	!Count number of lines in .nas file.
	i7 = 0
	ierr = 0
	num_lines = 0
	open(10,file=nasfile(1:len_trim(nasfile))//'.nas',form='formatted',status='old')

	do while (ierr == 0)
	  num_lines = num_lines + 1
	  read(10,*,iostat=ierr) 
	end do
	rewind(10)
	num_lines = num_lines - 1
	
! Read each line to check for PSHELL, GRID, CTRIA3
	do i7 = 1, num_lines
		read(10,*) string3, el2 
		if ( string3 == 'PSHELL' ) then
			nPshell = el2 !overwrites prev PSHELL number to get total number of PSHELLS
		end if 
	end do
	rewind(10)
	do i7 = 1, num_lines
		read(10,*) string3, el2
		if ( string3 == 'GRID' ) then
			np = el2
		end if 
	end do
	rewind(10)
	do i7 = 1, num_lines
		read(10,*) string3, el2
		if ( string3 == 'CTRIA3' ) then
			nbf = el2
		end if 
	end do
	rewind(10)

	 
! Read in data from .nas
     read(10,*) string
     read(10,*)
	 
     write(6,*) 'nPshell = ',nPshell
     do i=1,nPshell
       read(10,*) string
       write(*,*) 'Reading: ',string
     enddo
     allocate (coor(3,np))
     do ip=1,np
       read(10,*)   string,j,dummy,x,y,z
       write(*,*) 'Reading point ',j,'x=',x,'y=',y,'z=',z
       coor(1,ip)=x
       coor(2,ip)=y
       coor(3,ip)=z
     enddo
     allocate (iface(5,nbf))
     nsurf=0
     do i=1,nbf
       read(10,*) string,j,iface(5,i),iface(2,i),iface(3,i),iface(4,i)
       iface(1,i)=i
       if(iface(5,i).gt.nsurf) nsurf=iface(5,i)
       write(*,*) 'Reading face',j,'iface(:,*)=',iface(1,i),iface(2,i),iface(3,i),iface(4,i),iface(5,i)
     enddo
!
     close(10)

! Open new .fro file

    open(11,file=nasfile(1:len_trim(nasfile))//'.fro',form='formatted',status='unknown')

! write out fro file

    write(6,*) 'Writing out the new .fro file'
    write(11,*) nbf,np,1,0,0,nsurf,0,0
    do ip=1,np
      write(11,*) ip,(coor(in,ip),in=1,3)
    enddo
    do it=1,nbf
      write(11,*) (iface(in,it),in=1,5)
    enddo
    close(11)
    write(6,*) 'Finished - good luck with this!'

    end


