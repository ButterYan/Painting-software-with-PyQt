import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QMainWindow,QInputDialog,QPushButton,QLabel,QMessageBox,QHBoxLayout,
                             QVBoxLayout,QGridLayout,QFrame,QColorDialog,QAction, qApp,QFileDialog,QGraphicsItem,
                             QGraphicsLineItem,QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsPixmapItem, QGraphicsTextItem,
                             QGraphicsPathItem, QGraphicsScene, QGraphicsView,QDockWidget,QDoubleSpinBox)
from PyQt5.QtCore import Qt,QRect
from PyQt5.QtGui import QPen, QColor, QPixmap,QPainterPath,QIcon,QBrush,QImage
class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.line=[]
        self.linenum=0
        self.circle=[]
        self.circlenum=0
        self.ellipse=[]
        self.ellipsenum=0
        self.square=[]
        self.squarenum=0
        self.rect = []
        self.rectnum = 0
        self.pic=[]
        self.picnum=0
        self.picsave=[]
        self.text=[]
        self.textnum=0
        self.tri1=[]
        self.tri1num=0
        self.tri2=[]
        self.tri2num=0
        self.path=[]
        self.pathnum=0



    def newline(self,angle,length,scale,pen):
        self.line.insert(self.linenum,QGraphicsLineItem())
        self.line[self.linenum].setLine(100, 100, 100+length, 100)
        self.line[self.linenum].setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.line[self.linenum].setRotation(angle)

        b = self.line[self.linenum].boundingRect()
        b = b.center()
        self.line[self.linenum].setTransformOriginPoint(b)
        self.line[self.linenum].setScale(scale)
        self.line[self.linenum].setPen(pen)

        self.scene.addItem(self.line[self.linenum])
        self.linenum=self.linenum+1

    def newcircle(self,angle,length,pen,brush):
        self.circle.insert(self.circlenum,QGraphicsEllipseItem())
        self.circle[self.circlenum].setRect(100,100,length,length)
        self.circle[self.circlenum].setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.circle[self.circlenum].setRotation(angle)
        self.circle[self.circlenum].setPos(0, 0)
        self.circle[self.circlenum].setPen(pen)
        self.circle[self.circlenum].setBrush(brush)

        self.scene.addItem(self.circle[self.circlenum])
        self.circlenum=self.circlenum+1

    def newellipse(self,angle,length,height,scale,pen,brush):
        self.ellipse.insert(self.ellipsenum,QGraphicsEllipseItem())
        self.ellipse[self.ellipsenum].setRect(100, 100, length, height)
        self.ellipse[self.ellipsenum].setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.ellipse[self.ellipsenum].setRotation(angle)

        b = self.ellipse[self.ellipsenum].boundingRect()
        b = b.center()
        self.ellipse[self.ellipsenum].setTransformOriginPoint(b)
        self.ellipse[self.ellipsenum].setScale(scale)
        self.ellipse[self.ellipsenum].setPen(pen)
        self.ellipse[self.ellipsenum].setBrush(brush)

        self.scene.addItem(self.ellipse[self.ellipsenum])
        self.ellipsenum=self.ellipsenum+1


    def newsquare(self,angle,length,pen,brush):
        self.square.insert(self.squarenum, QGraphicsRectItem())
        self.square[self.squarenum].setRect(100, 100, length, length)
        self.square[self.squarenum].setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.square[self.squarenum].setRotation(angle)
        self.square[self.squarenum].setPen(pen)
        self.square[self.squarenum].setBrush(brush)

        self.scene.addItem(self.square[self.squarenum])
        self.squarenum = self.squarenum + 1

    def newrect(self,angle,length,height,scale,pen,brush):
        self.rect.insert(self.rectnum,QGraphicsRectItem())
        self.rect[self.rectnum].setRect(100,100, length, height)
        self.rect[self.rectnum].setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.rect[self.rectnum].setRotation(angle)

        b = self.rect[self.rectnum].boundingRect()
        b = b.center()
        self.rect[self.rectnum].setTransformOriginPoint(b)
        self.rect[self.rectnum].setScale(scale)
        self.rect[self.rectnum].setPen(pen)
        self.rect[self.rectnum].setBrush(brush)

        self.scene.addItem(self.rect[self.rectnum])
        self.rectnum = self.rectnum + 1


    def newtri1(self,angle,length,height,scale,pen,brush):
        self.tri1.insert(self.tri1num,QGraphicsPathItem())
        tri_path = QPainterPath()
        tri_path.moveTo(100, 100)
        tri_path.lineTo(100, 100+height)
        tri_path.lineTo(100+length, 100+height)
        tri_path.lineTo(100, 100)
        tri_path.closeSubpath()
        self.tri1[self.tri1num].setPath(tri_path)
        self.tri1[self.tri1num].setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.tri1[self.tri1num].setRotation(angle)

        b = self.tri1[self.tri1num].boundingRect()
        b = b.center()
        self.tri1[self.tri1num].setTransformOriginPoint(b)
        self.tri1[self.tri1num].setScale(scale)
        self.tri1[self.tri1num].setPen(pen)
        self.tri1[self.tri1num].setBrush(brush)

        self.scene.addItem(self.tri1[self.tri1num])
        self.tri1num=self.tri1num+1

    def newtri2(self,angle,length,height,scale,pen,brush):
        self.tri2.insert(self.tri2num,QGraphicsPathItem())
        tri_path = QPainterPath()
        tri_path.moveTo(100+length*0.5, 100)
        tri_path.lineTo(100+length, 100+height)
        tri_path.lineTo(100, 100+height)
        tri_path.lineTo(100+length*0.5, 100)
        tri_path.closeSubpath()
        self.tri2[self.tri2num].setPath(tri_path)
        self.tri2[self.tri2num].setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.tri2[self.tri2num].setRotation(angle)

        b = self.tri2[self.tri2num].boundingRect()
        b = b.center()
        self.tri2[self.tri2num].setTransformOriginPoint(b)
        self.tri2[self.tri2num].setScale(scale)
        self.tri2[self.tri2num].setPen(pen)
        self.tri2[self.tri2num].setBrush(brush)

        self.scene.addItem(self.tri2[self.tri2num])
        self.tri2num=self.tri2num+1


    def newpic(self,pic,angle,length,height,scale):
        self.picsave.insert(self.picnum,pic)
        self.pic.insert(self.picnum,QGraphicsPixmapItem())
        self.pic[self.picnum].setPixmap(self.picsave[self.picnum].scaled(length, height))
        self.pic[self.picnum].setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.pic[self.picnum].setOffset(100, 120)
        self.pic[self.picnum].setRotation(angle)

        b = self.pic[self.picnum].boundingRect()
        b = b.center()
        self.pic[self.picnum].setTransformOriginPoint(b)
        self.pic[self.picnum].setScale(scale)
        self.scene.addItem(self.pic[self.picnum])
        self.picnum=self.picnum+1


    def newtext(self,words,angle,scale,pen):
        self.text.insert(self.textnum,QGraphicsTextItem())
        self.text[self.textnum].setPlainText(words)
        self.text[self.textnum].setDefaultTextColor(pen)
        self.text[self.textnum].setPos(100, 100)
        self.text[self.textnum].setTextInteractionFlags(Qt.TextEditorInteraction)
        self.text[self.textnum].setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.text[self.textnum].setRotation(angle)
        self.text[self.textnum].setScale(scale)

        self.scene.addItem(self.text[self.textnum])
        self.textnum = self.textnum + 1


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
    def init(self):
        self.setWindowIcon(QIcon("pic.jpg"))
        #创建状态栏
        self.m = self.statusBar()
        self.m.showMessage('MyDraw is ready!')

        self.a = Demo()
        self.b = self.a.scene
        self.setCentralWidget(self.a)
        self.setGeometry(150, 150, 1160, 800)
        self.setWindowTitle('MyDraw')
        self.bgpic=None  #专门用于存放图片背景


        self.tool2 = self.addToolBar('b')
        self.tool2.addWidget(QLabel("创建:"))
        self.addline=QAction(QIcon("line.ico"),"直线",self)
        self.addline.triggered.connect(self.add6)

        self.addcircle = QAction(QIcon("circle.ico"), '圆', self)
        self.addcircle.triggered.connect(self.add4s)
        self.addellipse = QAction(QIcon("elli.ico"), '椭圆', self)
        self.addellipse.triggered.connect(self.add4)

        self.addsquare = QAction(QIcon("squ.ico"), '正方形', self)
        self.addsquare.triggered.connect(self.add3s)
        self.addrect = QAction(QIcon("rec.ico"), '长方形', self)
        self.addrect.triggered.connect(self.add3)

        self.addtri1 = QAction(QIcon("tri1.ico"), '直角三角形', self)
        self.addtri1.triggered.connect(self.add21)
        self.addtri2 = QAction(QIcon("tri2.ico"), '等腰三角形', self)
        self.addtri2.triggered.connect(self.add22)

        self.addpic = QAction(QIcon("pic.jpg"), '图片', self)
        self.addpic.triggered.connect(self.add7)

        self.addtext = QAction(QIcon("text.ico"), '文字', self)
        self.addtext.triggered.connect(self.add8)

        adds=[self.addline,self.addcircle,self.addellipse,self.addsquare,self.addrect,self.addtri1,
              self.addtri2,self.addpic,self.addtext]
        self.tool2.addActions(adds)
        for i in adds:
            i.setIconVisibleInMenu(False)

        #以下是在选中对象条件下的状态栏，
        self.tool=self.addToolBar('a')
        self.tool.addWidget(QLabel("设置:"))
        self.dele=QAction(QIcon("删除.ico"),'删除',self)
        self.dele.setShortcut('delete')
        self.dele.triggered.connect(self.delefun)
        self.clone=QAction(QIcon("克隆.ico"),"克隆",self)
        self.clone.setShortcut('Ctrl+V')
        self.clone.triggered.connect(self.clonefun)

        self.shrink = QAction(QIcon("缩小.ico"), '缩小(-)', self)
        self.shrink.setShortcut('-')
        self.shrink.triggered.connect(self.changefun)
        self.expand = QAction(QIcon("放大.ico"), '放大(+)', self)
        self.expand.setShortcut('+')
        self.expand.triggered.connect(self.changefun)

        self.left=QAction(QIcon("逆时针旋转90°.ico"),'逆时针旋转90°',self)
        self.left.setShortcut('Ctrl+L')
        self.left.triggered.connect(self.changefun)
        self.reverse = QAction(QIcon("旋转180°.ico"), '旋转180°', self)
        self.reverse.setShortcut('Ctrl+U')
        self.reverse.triggered.connect(self.changefun)
        self.right = QAction(QIcon("顺时针旋转90°.ico"), '顺时针旋转90°', self)
        self.right.triggered.connect(self.changefun)
        self.right.setShortcut('Ctrl+R')

        changes=[self.dele,self.clone,self.shrink,self.expand,self.left,self.reverse,self.right]
        self.tool.addActions(changes)
        for i in changes:
            i.setIconVisibleInMenu(False)


        # 菜单栏
        self.menubar = self.menuBar()
        # 文件菜单
        file = self.menubar.addMenu('文件')
        exit = QAction('Exit', self)  # 建立exit按钮
        exit.setShortcut('Ctrl+Q')  # 快捷键
        exit.triggered.connect(self.exitfun)  # 触发quit操作
        bg = QAction('背景', self)
        bg.setShortcut('Ctrl+B')
        bg.triggered.connect(self.bgfun)
        open = QAction('打开', self)
        open.setShortcut('Ctrl+O')
        open.triggered.connect(self.openfun)
        save = QAction('保存', self)
        save.setShortcut('Ctrl+S')
        save.triggered.connect(self.savefun)
        file.addAction(open)
        file.addAction(save)
        file.addAction(bg)
        file.addAction(exit)
        #插入菜单
        insert = self.menubar.addMenu('插入')
        insert.addActions(adds)


        setup = self.menubar.addMenu('设置')
        setup.addActions(changes)

        col_to=QAction("恢复默认页面颜色",self)
        col_to.setShortcut('R')
        col_to.triggered.connect(self.colret)
        setup.addAction(col_to)



        guide = self.menubar.addMenu('帮助')  # 编写一个指南

        nfun = QAction('特色功能帮助', self)
        nfun.setShortcut('Ctrl+H')
        nfun.triggered.connect(self.funfun)
        helping = QAction('对象特性', self)
        helping.setShortcut('Ctrl+N')
        helping.triggered.connect(self.obspfun)
        #exit.setShortcut('Ctrl+Q')  # 快捷键
        #exit.triggered.connect(self.exitfun)
        shortcut = QAction('快捷键列表',self)
        shortcut.setShortcut('H')
        shortcut.triggered.connect(self.scutfun)
        guide.addActions([nfun,helping,shortcut])


        self.dock=QDockWidget("工具",self)
        self.dock.setFixedHeight(80)
        self.addDockWidget(Qt.TopDockWidgetArea,self.dock)
        self.dock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.subdock=QWidget()
        self.dock.setWidget(self.subdock)
        grid=QGridLayout()
        grid.setContentsMargins(1,0,8,0)
        self.subdock.setLayout(grid)

        grid.addWidget(self.tool2,0,0,1,2)
        grid.addWidget(self.tool,1,0)
        length0=QLabel("长度缩放:")
        self.length1=QDoubleSpinBox()
        self.length1.setRange(0,10)
        self.length1.setSingleStep(0.1)
        self.length1.setAccelerated(True)
        self.length1.setSuffix("倍")
        height0=QLabel("高度缩放:")
        self.height1=QDoubleSpinBox()
        self.height1.setRange(0,10)
        self.height1.setSingleStep(0.1)
        self.height1.setAccelerated(True)
        self.height1.setSuffix("倍")
        angl0=QLabel("角度:")
        self.angl1=QDoubleSpinBox()
        self.angl1.setRange(0,360)
        self.angl1.setSingleStep(5)
        self.angl1.setAccelerated(True)
        self.angl1.setSuffix("度")
        self.angl1.setWrapping(True)  #设置循环展示
        angtool=QHBoxLayout()
        angtool.addWidget(angl0)
        angtool.addWidget(self.angl1)
        grid.addLayout(angtool,1,1)

        lengthtool=QHBoxLayout()
        lengthtool.addWidget(length0)
        lengthtool.addWidget(self.length1)
        grid.addLayout(lengthtool,0,3)

        heighttool=QHBoxLayout()
        heighttool.addWidget(height0)
        heighttool.addWidget(self.height1)
        grid.addLayout(heighttool,1,3)


        self.preview=QLabel()   #一个预览边框与填充色的label
        self.colin=QColor(255,255,255)
        self.colout=QColor(0,0,0)
        self.preview.setFixedSize(42,42)

        self.cs = self.addToolBar('col')
        self.penc = QAction(QIcon("边框.ico"), "边框色", self)
        self.penc.setCheckable(True)
        self.penc.triggered.connect(self.pencfun)
        self.brushc = QAction(QIcon("填充.ico"), "填充色", self)
        self.brushc.setCheckable(True)
        self.brushc.triggered.connect(self.brushfun)

        self.cs.addAction(self.penc)
        self.cs.addAction(self.brushc)

        self.chose = QPushButton("更多颜色")
        self.chose.setFixedWidth(80)
        self.chose.clicked.connect(self.chosefun)

        c1=self.addToolBar('c1')
        c2 = self.addToolBar('c2')
        self.c_wid=[]   #存储常用颜色小部件
        strcol=["白色","灰色","红色","绿色","蓝色","黄色","橙色","黑色","浅灰","深红","深绿","深蓝","土黄","深紫"]
        for i in range(0,14):
            self.c_wid.insert(i,QAction(QIcon(str(i+1)+".jpg"),strcol[i],self))
            self.c_wid[i].triggered.connect(self.colbarfun)
            if i<7:
                c1.addAction(self.c_wid[i])
            else:
                c2.addAction(self.c_wid[i])


        grid.addWidget(self.preview, 0, 4, 2, 1)
        grid.addWidget(self.cs,0,5)
        grid.addWidget(self.chose,1,5)
        grid.addWidget(c1,0,6)
        grid.addWidget(c2,1,6)

        self.ret=QPushButton("恢复默认")
        self.ret.clicked.connect(self.returnfun)
        self.sure = QPushButton()
        self.sure.setText("应用设置")
        self.sure.setShortcut(Qt.Key_Return)  #大键盘上的enter，小键盘上的是Qt.Key_Enter
        self.sure.clicked.connect(self.setfun)


        grid.addWidget(self.ret,0,7)
        grid.addWidget(self.sure,1,7)
        grid.setHorizontalSpacing(12)
        grid.setVerticalSpacing(2)


        self.returnfun()
        self.setsize()
        self.a.resize(self.corewidth,self.coreheight)
        self.b.setSceneRect(0,0,self.corewidth,self.coreheight)


        self.show()

    def setsize(self):
        self.corewidth = self.width() - 2
        self.coreheight = self.height() - 12 - self.menubar.height() - self.dock.height()- self.m.height()
    def bgfun(self,event):
        col = QColorDialog.getColor()
        if col.isValid():
            brush=QBrush(col)
            self.b.setBackgroundBrush(brush)
    def exitfun(self,event):
        reply= QMessageBox.question(self,"MyDraw","是否保存本次编辑",QMessageBox.Yes|QMessageBox.No)
        if reply== QMessageBox.No:
            qApp.quit()
    def openfun(self,event):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        if fname[0]:
            self.bgpic = QPixmap()
            self.bgpic.load(str(fname[0]))
            self.setsize()
            image = self.bgpic.scaled(self.corewidth, self.coreheight)
            brush = QBrush(image)
            self.b.setBackgroundBrush(brush)
    def savefun(self,event):
        fname = QFileDialog.getSaveFileName(self, 'Open file')
        self.m.showMessage(str(fname[0]))
        if fname[0]:
            image=QImage()
            self.b.clearSelection()
            self.setsize()
            image = self.a.grab(QRect(2,2,self.corewidth-2,self.coreheight-2))
            image.save(str(fname[0]))

    def delefun(self):
        if self.b.selectedItems():
            for i in self.b.selectedItems():
                self.b.removeItem(i)
    def clonefun(self):
        if self.b.selectedItems():
            for i in self.b.selectedItems():
                if i.type()==6:
                    self.a.newline(i.rotation(), i.line().length(), i.scale(), i.pen())
                if i.type()==4:
                    self.a.newellipse(i.rotation(), i.boundingRect().width(), i.boundingRect().height(), i.scale(),
                                      i.pen(), i.brush())
                if i.type() == 3:
                    self.a.newrect(i.rotation(),i.boundingRect().width(),i.boundingRect().height(),i.scale(),
                                   i.pen(),i.brush())
                if i.type()==2:
                    if i in self.a.tri1:
                        self.a.newtri1(i.rotation(),i.boundingRect().width(),i.boundingRect().height(),i.scale(),
                                       i.pen(),i.brush())
                    if i in self.a.tri2:
                        self.a.newtri2(i.rotation(),i.boundingRect().width(),i.boundingRect().height(),i.scale(),
                                       i.pen(),i.brush())
                if i.type()==7:
                    for j in range(0, self.a.picnum):
                        if self.a.pic[j] == i:
                            self.a.newpic(self.a.picsave[j], i.rotation(),
                                          i.boundingRect().width(), i.boundingRect().height(),i.scale())
                            break
                if i.type()==8:
                    self.a.newtext(i.toPlainText(), i.rotation(), i.scale(), i.defaultTextColor())


    def changefun(self):
        sender = self.sender()
        if self.b.selectedItems():
            for i in self.b.selectedItems():
                b = i.boundingRect()
                b=b.center()
                i.setTransformOriginPoint(b)
                if sender==self.left:
                    i.setRotation(i.rotation()+270)
                elif sender==self.reverse:
                    i.setRotation(i.rotation()+180)
                elif sender==self.right:
                    i.setRotation(i.rotation()+90)
                elif sender==self.shrink:
                    i.setScale(0.9*i.scale())
                elif sender==self.expand:
                    i.setScale(1/0.9*i.scale())


    def resizeEvent(self, event):
        self.setsize()
        self.a.setSceneRect(0,0,self.corewidth,self.coreheight)
        self.b.setSceneRect(0,0,self.corewidth,self.coreheight)
        if self.bgpic:
            image=self.bgpic.scaled(self.corewidth, self.coreheight)
            brush = QBrush(image)
            self.b.setBackgroundBrush(brush)

    def chosefun(self):          #用取色版选颜色按钮
        if self.penc.isChecked() or self.brushc.isChecked():
            col = QColorDialog.getColor()
            if col.isValid():
                if self.brushc.isChecked():
                    self.colin=col
                else:
                    self.colout=col
                self.previewfun()
        else:
            QMessageBox.information(self,'提示','请从上面的小图标中选择设置颜色的对象')

    def pencfun(self):
        self.brushc.setChecked(False)
    def brushfun(self):
        self.penc.setChecked(False)

    def previewfun(self):
        self.preview.setAutoFillBackground(True)
        a = QColor.getRgb(self.colout)
        b = QColor.getRgb(self.colin)
        self.preview.setFrameShadow(QFrame.Raised)
        self.preview.setStyleSheet('border-width: 2px;border-style: solid;'+
                                   'border-color: rgb(' +str(a[0]) + ',' + str(a[1]) + ',' + str(a[2]) + ');'+
                                   'background-color: rgb('+str(b[0]) + ',' + str(b[1]) + ',' + str(b[2]) + ');')

    def colbarfun(self):
        seq=[QColor(255,255,255),QColor(128,128,128),QColor(255,0,0),QColor(0,255,0),
             QColor(0,0,255),QColor(255,255,0),QColor(255,85,0),
             QColor(0,0,0),QColor(192,192,192),QColor(128,0,0),QColor(0,128,0),
             QColor(0,0,128),QColor(128,128,0),QColor(128,0,128)]
        sender=self.sender()
        for i in range(0,14):
            if sender==self.c_wid[i]:
                if self.brushc.isChecked():
                    self.colin=seq[i]
                if self.penc.isChecked():
                    self.colout=seq[i]
                self.previewfun()
    def returnfun(self):     #两部分，把颜色设回默认，把参数设回默认
        self.colret()
        self.numret()
    def colret(self):
        self.colin = QColor(255, 255, 255)
        self.colout = QColor(0, 0, 0)
        self.previewfun()
    def numret(self):
        self.length1.setValue(1)
        self.height1.setValue(1)
        self.angl1.setValue(0)
    def setfun(self):
        #图像的类型：直线：6，椭圆：4，矩形：3，path：2，图片：7，文字：8
        if self.b.selectedItems():
            for i in self.b.selectedItems():
                b = i.boundingRect()
                b_c = b.center()
                i.setTransformOriginPoint(b_c)
                if self.angl1.value()!=0 and self.angl1.value()!=360:
                    i.setRotation(i.rotation() + self.angl1.value())
                if i.type()==6:
                    i.setScale(self.length1.value()*i.scale())
                    pen=QPen(self.colout)
                    i.setPen(pen)
                elif i.type()==7:
                    w=b.width()*self.length1.value()
                    h=b.height()*self.height1.value()
                    for j in range(0,self.a.picnum):
                        if self.a.pic[j]==i:
                            i.setPixmap(self.a.picsave[j].scaled(w,h))
                elif i.type()==8:
                    h=b.height()
                    i.setScale(self.height1.value()*i.scale())
                    i.setDefaultTextColor(self.colout)
                elif i.type()==2:
                    i.setScale(self.length1.value()*i.scale())
                    i.setBrush(QBrush(self.colin))
                    i.setPen(QPen(self.colout))
                else:
                    #if self.length1.value()!=1 or self.height1.value()!=1:
                    w = b.width()*self.length1.value()
                    h = b.height()*self.height1.value()
                    i.setRect(b_c.x()-w/2,b_c.y()-h/2,w-1,h-1)
                    i.setBrush(QBrush(self.colin))
                    i.setPen(QPen(self.colout))
            self.numret()
        else:
            QMessageBox.information(self, '提示', '请先选择需要设置的对象')

    def add6(self):
        self.a.newline(self.angl1.value(), self.length1.value()*100,1, self.colout)
    def add4s(self):
        self.a.newcircle(self.angl1.value(), self.length1.value()*60, self.colout, self.colin)
    def add4(self):
        self.a.newellipse(self.angl1.value(), self.length1.value()*100, self.height1.value()*30, 1, self.colout, self.colin)
    def add3s(self):
        self.a.newsquare(self.angl1.value(), self.length1.value()*60, self.colout, self.colin)
    def add3(self):
        self.a.newrect(self.angl1.value(), self.length1.value()*100, self.height1.value()*30, 1, self.colout, self.colin)
    def add21(self):
        self.a.newtri1(self.angl1.value(), self.length1.value()*60, self.height1.value()*60, 1, self.colout, self.colin)
    def add22(self):
        self.a.newtri2(self.angl1.value(), self.length1.value()*60, self.height1.value()*60, 1, self.colout, self.colin)
    def add7(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            file=fname[0]
            self.a.newpic(QPixmap(file),self.angl1.value(), self.length1.value()*60, self.height1.value()*60,1)
    def add8(self):
        text, ok = QInputDialog.getText(self, '添加文字','请输入文字内容')
        if ok:
            self.a.newtext(str(text),self.angl1.value(), self.height1.value(),self.colout)

    def scutfun(self):
        self.scutwin = scut()
        self.scutwin.setHidden(True)
        self.scutwin.fun3()
        self.scutwin.show()
    def obspfun(self):
        self.scutwin = scut()
        self.scutwin.setHidden(True)
        print(2)
        self.scutwin.fun2()
        self.scutwin.show()
    def funfun(self):
        self.scutwin = scut()
        self.scutwin.setHidden(True)
        self.scutwin.fun1()
        self.scutwin.show()

class scut(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
    def init(self):
        self.setGeometry(200, 200, 400, 450)
        self.setWindowIcon(QIcon("pic.jpg"))


        self.num=[]

        self.hbox =QHBoxLayout()
        self.sure = QPushButton("关闭")
        self.sure.clicked.connect(self.close)
        self.hbox.addWidget(self.sure)

        self.show()

    def fun3(self):
        self.num=3
        self.vbox3 = QVBoxLayout()
        self.setLayout(self.vbox3)
        key=['Ctrl+O','Ctrl+S','Ctrl+B','Ctrl+Q','Delete','Ctrl+V','-','+','Ctrl+L','Ctrl+R','Ctrl+U',
             'Ctrl+H','Ctrl+N','H','R','Enter']
        oper=["打开","保存","背景","退出","删除","克隆","缩小","放大","逆时针旋转90°","顺时针旋转90°","旋转180°",
              "特色功能","对象特性","快捷键列表","恢复默认颜色","应用设置"]
        hbox=[]
        for i in range(0,16):
            hbox.insert(i,QHBoxLayout())
            hbox[i].addWidget(QLabel(key[i]+':'))
            hbox[i].addWidget(QLabel(oper[i]))
            self.vbox3.addLayout(hbox[i])
        self.vbox3.addLayout(self.hbox)
        self.setWindowTitle('快捷键列表')
    def fun2(self):
        self.num=2
        self.vbox2 = QVBoxLayout()
        self.setLayout(self.vbox2)
        grid=QGridLayout()
        nam=['','角度','长度','高度','边框色','填充色','备注',
             '直线','√','√','×','√','×','边框色即为线条颜色',
             '圆','√','√','√','√','√','可通过伸缩变成椭圆',
             '椭圆','√','√','√','√','√','',
             '正方形','√','√','√','√','√','可通过伸缩变成长方形',
             '长方形','√','√','√','√','√','',
             '三角形','√','√','×','√','√','三角形只可以等比放缩,请创建时设定好比例。',
             '图片','√','√','√','×','×','',
             '文字','√','×','√','√','×','高度设置字体大小，边框色设置颜色，暂不支持修改内容']
        for i in range(0,63):
            lab=QLabel(nam[i])
            lab.setAlignment(Qt.AlignCenter)
            lab.setWordWrap(True)
            grid.addWidget(lab,i//7,i%7)

        lab=QLabel("注:√代表对该对象的该项设置是有意义的，×代表无意义。")
        grid.addWidget(lab,9,0,1,7)
        self.vbox2.addLayout(grid)
        self.vbox2.addLayout(self.hbox)

        self.setWindowTitle('对象特性')
    def fun1(self):
        self.num=1
        self.vbox1 = QVBoxLayout()
        self.setLayout(self.vbox1)
        self.vbox1.addStretch(1)
        nam = ['1、设置工具栏提供了删除和克隆功能，克隆功能将在默认位置复制出与选中对象完全相同的对象。',
               '2、设置工具栏提供了一键旋转与一键方法功能，直角旋转与等比放缩可一键搞定。',
               '3、边框与填充色的设置提供预览，点击应用设置键可设置选中对象，恢复默认按钮可一键恢复默认颜色预览。',
               '4、除插入工具外，其余操作均提供快捷键，快捷键H可查看全部快捷键。']
        for i in range(0, 4):
            lab = QLabel(nam[i])
            lab.setAlignment(Qt.AlignLeft)
            lab.setWordWrap(True)
            self.vbox1.addWidget(lab)
            self.vbox1.addStretch(1)
        self.vbox1.addLayout(self.hbox)
        self.setWindowTitle('特色功能')









if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    ex.show()
    sys.exit(app.exec_())





''''尚未完成的：
1、窗口图标，指南(设置与创建逻辑，直线图片字体的特殊情况)与快捷键列表
2、撤销
3、更多对象（多边形，圆角四边形，箭头)

4、抠图'''



