#include "mainwindow.h"
#include <QApplication>

//first char must not be a space
//when no representable char is found, use º

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    return a.exec();
}
