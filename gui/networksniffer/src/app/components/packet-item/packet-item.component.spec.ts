import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PacketItemComponent } from './packet-item.component';

describe('PacketItemComponent', () => {
  let component: PacketItemComponent;
  let fixture: ComponentFixture<PacketItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PacketItemComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PacketItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
