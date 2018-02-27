package com.hashmapinc.tempus.clientdevice.services;

import com.hashmapinc.tempus.clientdevice.context.ApplicationContext;
import com.hashmapinc.tempus.clientdevice.dao.AppConfigDao;
import org.apache.log4j.Logger;

import java.util.Map;

public class ApplicationService {

    AppConfigDao appConfigDao = new AppConfigDao();
    public void initConfig()
    {
        appConfigDao.createApplicationTables();
    }

    public Map<String,String> getContext() {
        return appConfigDao.getContext();
    }

    public String getDeviceId() {
        return appConfigDao.getDeviceId();
    }

    public void configureDevice(String name, String password, String serverIP, String port) {
        appConfigDao.configureDevice(name,password,serverIP,port);
        ApplicationContext.getContext().getCommunicationManager().start();
    }
}