#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <samplebox.h>

#include <QList>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

public slots:
    void nextKeyChar();
    void prevKeyChar();
    void prevChar();
    void nextChar();
    void keyChanged();
    void loadSamples();

signals:
    void highlightChar(int idx);
    void calculate(QString key);

private:
    Ui::MainWindow *ui;
    int keyIdx;
    QList<QString> *SAMPLES;
    QString *KEY;

    QList<sampleBox*> samples;
};

#endif // MAINWINDOW_H
