import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ArptablesComponent } from './arptables.component';

describe('ArptablesComponent', () => {
  let component: ArptablesComponent;
  let fixture: ComponentFixture<ArptablesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ArptablesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ArptablesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
