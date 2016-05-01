#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QBoxLayout>
#include <QVBoxLayout>
#include <QString>
#include <QList>

#include <QDebug>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    loadSamples();

    keyIdx = -1;
    nextKeyChar();
    emit calculate(ui->key->toPlainText());
    QObject::connect(ui->Prev, SIGNAL(clicked(bool)), this, SLOT(prevKeyChar()));
    QObject::connect(ui->Next, SIGNAL(clicked(bool)), this, SLOT(nextKeyChar()));
    QObject::connect(ui->PrevReplace , SIGNAL(clicked(bool)), this, SLOT(prevChar()));
    QObject::connect(ui->NextReplace , SIGNAL(clicked(bool)), this, SLOT(nextChar()));
    QObject::connect(ui->lineEdit, SIGNAL(textChanged(QString)), this, SLOT(keyChanged()));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::nextKeyChar()
{
    QString text = ui->key->toPlainText();
    if (text.length() == 0)
        return;

    keyIdx = (keyIdx + 1) % text.length();
    ui->key->clear();

    if (text.at(keyIdx) == '<')
        ui->key->setPlainText(text);
    else
        ui->key->setHtml(sampleBox::highLight(text, keyIdx));

    ui->lineEdit->clear();
    ui->lineEdit->setText(text.at(keyIdx));
    emit highlightChar(keyIdx);
}

void MainWindow::prevKeyChar()
{
    QString text = ui->key->toPlainText();
    if (text.length() == 0)
        return;

    keyIdx = keyIdx - 1;
    if (keyIdx < 0)
        keyIdx = text.length()-1;

    ui->key->clear();

    if (text.at(keyIdx) == '<')
        ui->key->setPlainText(text);
    else
        ui->key->setHtml(sampleBox::highLight(text, keyIdx));

    ui->lineEdit->clear();
    ui->lineEdit->setText(text.at(keyIdx));
    emit highlightChar(keyIdx);
}

void MainWindow::prevChar()
{
    if (ui->lineEdit->text().length() == 0)
        return;

    int current = (int)ui->lineEdit->text().at(0).toLatin1();
    if (current == 0x20)
        current = 0x7e;
    else
        current--;

    QChar qc((char)current);
    ui->lineEdit->clear();
    ui->lineEdit->setText(qc);
}

void MainWindow::nextChar()
{
    if (ui->lineEdit->text().length() == 0)
        return;

    int current = (int)ui->lineEdit->text().at(0).toLatin1();
    if (current == 0x7e)
        current = 0x20;
    else
        current++;

    QChar qc((char)current);
    ui->lineEdit->clear();
    ui->lineEdit->setText(qc);
}

void MainWindow::keyChanged()
{
    if (ui->lineEdit->text().length() == 0)
        return;

    QString text = ui->key->toPlainText();
    qDebug() << "replace " << text.at(keyIdx) << " By " << ui->lineEdit->text().at(0);

    QChar letter = ui->lineEdit->text().at(0);
    text.replace(keyIdx, 1, letter);

    ui->key->clear();
    if (text.at(keyIdx) == '<')
        ui->key->setPlainText(text);
    else
        ui->key->setHtml(sampleBox::highLight(text, keyIdx));

    emit calculate(ui->key->toPlainText());
}

void MainWindow::loadSamples()
{
    int maxLength = 0;
    QStringList list = QStringList();
    list.append("3939252352554c5f51592621294d5c5229382f5d454b485d4554413132275458482d3157415046495c5b2a435a46543527364d5059394847382a2b4b555746404a38202d4c525652455c2a");
    list.append("4d514c503134405f305f4e44292c41534a57414f2c2c2d4054544d5f552741424c5931345f415d2c2e4d4454405e504142522e31424a434c5f2a2b415a412f585a55452d2e20394941562a");
    list.append("56574023455d4449305b4745295b5b5a45385f59435a44574526453132445c5a454843404d585a2c4146464e3246544146554531445c49574a435f573a");
    list.append("505725575951292c53594f515d435544484847522c2c4e5f4155575441274c45582d465d444c2e404b495859324f4f4227424131545644444d594e2e554a4b2c4757204947465f4c53572a");
    list.append("4d5625565f504c5e435f474f4d2c565f5a5b5d4e58492d4352494650504e59435954315d5b2047415e4758435349543553592e44595d4f504b5e4a4050244c5e4a48544249525849484b2a");
    list.append("5c57424f5847412c5c4e52554c5e41364f4a4a5a594943505926455d5e4842592d545e412854412c4c5a4f565927565c40534054455c2a43564e2b4d55415c4d413843445e485c4b533c");
    list.append("5a4b5c53455b4e5e515b4e5829454136594a4a584942593349482442575150584c413150414648495c4d44433253594542452e5e51394b524846424d555046435d4b20434157585d414b5722");
    list.append("505f255a5e41294a5f5e484529585a532957414e2c58445e45265450562b355e45485f34514f5b2c46495c523241495b4e45465453395e4a51592b2e574b5a5e405d57425c4b37");
    list.append("5c6f607168346a607f7e6221616d613668387c62607a6861206a6d7f7b697224");

    QVBoxLayout * layout = new QVBoxLayout();
    for (int i = 0; i < list.length(); i++)
    {
        QByteArray line = QByteArray::fromHex(list.at(i).toStdString().c_str());
        if (line.toStdString().length() > maxLength)
            maxLength = line.toStdString().length();

        qDebug() << QString::fromStdString(line.toStdString());

        sampleBox * sbox = new sampleBox(QString::fromStdString(line.toStdString()));
        QObject::connect(this, SIGNAL(highlightChar(int)), sbox, SLOT(selectChar(int)));
        QObject::connect(this, SIGNAL(calculate(QString)), sbox, SLOT(calculateXor(QString)));
        samples.append(sbox);
        layout->addWidget(sbox);

    }
    QString key = "key";
    while (key.length() < maxLength)
        key = key + "?";
    ui->key->clear();
    ui->key->setPlainText(key);
    ui->widget->setLayout(layout);
}

