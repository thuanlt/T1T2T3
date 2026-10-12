# RAID definition (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/metal-cloud/tutorials/raid/

# RAID definition

RAID (Redundant Array of Independent Disks) is a method of configuring member drives to create high availability and high performance systems. The RAID level provides different degrees of redundancy and performance; it also determines the number of members in the array.

The RAID level determines the relationship of the disks.

Level| Description| Drive count| Approximate array capacity| Redundancy*| RAID 0| Combines two or more disks by striping data across them. Chunks of data are written to each disk in the array alternately.| 1 - 8| Drive count × Drive size| None| RAID 1| A configuration that mirrors data between two or more disks. Everything written to the array is placed on each device in the group, so each disk has a complete set of the available data.| 2| Drive size| 1  
---|---|---|---|---  
  
*Redundancy indicates how many drive failures the array can tolerate. In some circumstances, an array can tolerate more than 1 drive failure.
