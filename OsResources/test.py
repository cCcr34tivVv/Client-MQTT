from OsResources import OS_Resources

if __name__ == '__main__':
    '''
    ceva=OS_Resources().get_cpu_percent(1,True)
    ceva0=OS_Resources().get_cpu_times(False)
    ceva1=OS_Resources().get_cpu_times_percent(1,False)
    ceva2=OS_Resources().get_cpu_count(True)
    ceva3=OS_Resources().get_cpu_freq(False)
    ceva4=OS_Resources().get_cpu_stats()
    ceva5=OS_Resources().get_load_avg()
    print(ceva)
    print(ceva0)
    print(ceva1)
    print(ceva2)
    print(ceva3)
    print(ceva4)
    print(ceva5)
    '''
    '''
    lala=OS_Resources().get_virtual_memory()
    lala0=OS_Resources().get_swap_memory()
    print(lala)
    print(lala0)
    '''
    '''
    f=OS_Resources().get_disk_partitions(True)
    f1=OS_Resources().get_disk_usage('/')
    f2=OS_Resources().get_disk_io_counters(True, True)
    print(f)
    print(f1)
    print(f2)
    '''
    '''
    c=OS_Resources().get_net_io_counters(False,False)
    c1=OS_Resources().get_net_connections('inet')
    print(c)
    print(c1)
    '''
    '''
    d=OS_Resources().get_sensors_temperatures(False)
    d1=OS_Resources().get_sensors_fans()
    d2=OS_Resources().get_sensors_battery()
    print(d)
    print(d1)
    print(d2)
    '''
    '''
    x=OS_Resources().get_boot_time()
    x1=OS_Resources().get_users()
    print(x)
    print(x1)
    '''