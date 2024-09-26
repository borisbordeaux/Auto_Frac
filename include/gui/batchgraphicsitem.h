#ifndef AUTOFRAC_BATCHGRAPHICSITEM_H
#define AUTOFRAC_BATCHGRAPHICSITEM_H

#include <QOpenGLFunctions>
#include "gui/camera.h"
#include "gui/pickingtype.h"

class BatchGraphicsItem : protected QOpenGLFunctions {
public:
    explicit BatchGraphicsItem() = default;

    virtual ~BatchGraphicsItem() = default;

    virtual void init() {}

    virtual void update() {}

    virtual void updateData() {}

    virtual void render(PickingType /*type*/ = PickingType::PickingNone) {}

    virtual void setProjection(QMatrix4x4 /*projection*/) {}

    virtual void setCamera(Camera /*camera*/) {}

    virtual void setLight(QVector3D /*lightPos*/) {}

    virtual int layer() { return 0; }
};


#endif //AUTOFRAC_BATCHGRAPHICSITEM_H
