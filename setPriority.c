#include "types.h"
#include "stat.h"
#include "user.h"
#include "fcntl.h"

int
main(int argc, char *argv[])
{
  int new_priority, pid;
  if(argc < 3){
    printf(2,"Usage: setPriority new_priority pid\n");
    exit();
  }
  new_priority = atoi(argv[1]);
  pid = atoi(argv[2]);
//   if (new_priority < 0 || new_priority > 20){
//     printf(2,"Invalid priority (0-20)!\n");
//     exit();
//   }
printf(1,"priority new = %d \n pid=%d \n",new_priority,pid);
  set_priority(new_priority,pid);
  exit();
}