import glob, numpy, os, math, re

part_list = glob.glob("C:\\Users\\boot\\Desktop\\HW\\New_Project\\Data\\*")

print "Participant Number\t", "Number of Collisions\t", "Mean Speed\t", "SD Speed\t", "Mean Lane Deviation\t", "SD Lane Deviation\t\n" 

# Participant level loop.
for part in part_list:
  pattern = re.search("\\\\Data\\\\(\d+)", part)
  part_number =  pattern.group(1) 

  
  # Initializing Lists.
  coll_list = [] 
  mean_speed_list = []
  sd_speed_list = []
  sum_of_squares1 = []
  mean_ld_list = []
  sum_of_squares2 = []

  

  # File Level Loop 1.
  file_name1 = part + "\\SCC_Collision_Count.txt"
  coll_file = open(file_name1, "r")

  # File Level Loop 2.
  file_name2 = part + "\\SCC_DynObj_Name.txt"
  dyn_obj_name_file = open(file_name2, "r")
  
  # File Level Loop 3.
  file_name3 = part + "\\SCC_DynObj_Pos.txt"
  dyn_obj_pos_file = open(file_name3, "r")

  #File Level Loop 4.
  file_name4 = part + "\\VDS_Veh_Speed.txt"
  veh_speed = open(file_name4, "r")

  #File Level Loop 5.
  file_name5 = part + "\\SCC_Lane_Deviation.txt"
  lane_dev = open(file_name5, "r")
  
  # Number of Collisions.
  for line in coll_file:
      line = line.split('\t') 
      line[1] = float(line[1])
      coll_list.append(line[1])
  coll_count = max(coll_list)
  
  # Mean Speed
  for mean_speed in veh_speed:
    mean_speed = mean_speed.split('\t')
    mean_speed[1] = float(mean_speed[1])
    mean_speed_list.append(mean_speed[1])
  sum_mean_speed = sum(mean_speed_list)
  length_mean_speed = len(mean_speed_list)
  m_speed = sum_mean_speed/length_mean_speed

  # SD Speed
  for item in mean_speed_list:
    ss1 = (item - m_speed)**2
    sum_of_squares1.append(ss1)
  real_sum_of_ss1 = sum(sum_of_squares1)
  sd1 = math.sqrt(real_sum_of_ss1 / (length_mean_speed - 1) )

  # Mean Lane Deviation
  for mean_ld in lane_dev:
    mean_ld = mean_ld.split('\t')
    mean_ld[1] = float(mean_ld[1])
    mean_ld_list.append(mean_ld[1])
  sum_mean_ld = sum(mean_ld_list)
  length_mean_ld = len(mean_ld_list)
  m_ld = sum_mean_ld/length_mean_ld

  # SD Lane Deviation
  for item in mean_ld_list:
    ss2 = (item - m_ld)**2
    sum_of_squares2.append(ss2)
  real_sum_of_ss2 = sum(sum_of_squares2)
  sd2 = math.sqrt(real_sum_of_ss2 / (length_mean_ld - 1) )
  

  print "\t", part_number, "\t\t\t", coll_count,  "\t\t\t", m_speed, "\t\t\t", sd1, "\t\t\t", m_ld, "\t\t\t", sd2, "\n"
